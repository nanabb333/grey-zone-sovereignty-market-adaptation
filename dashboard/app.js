const dashboardDataPath = "../results/dashboard_data.csv";
const executiveSummaryPath = "../results/executive_summary.md";
const eventInsightsPath = "../results/event_insights.json";
const llmContextPath = "../results/llm_context.json";
const historicalComparisonPath = "../results/historical_comparison.json";
const executiveBriefPath = "../results/executive_brief.json";

const formatPercent = (value) => {
  const number = Number(value);
  if (Number.isNaN(number)) return "N/A";
  return `${number.toFixed(2)}%`;
};

const parseCsv = (text) => {
  const rows = text.trim().split(/\r?\n/);
  const headers = rows.shift().split(",");
  return rows.map((row) => {
    const values = row.split(",");
    return headers.reduce((record, header, index) => {
      record[header] = values[index] ?? "";
      return record;
    }, {});
  });
};

const getStrongestPositive = (events) =>
  events
    .filter((event) => event.status === "success" && Number(event.car_value) > 0)
    .sort((a, b) => Number(b.car_value) - Number(a.car_value))[0];

const getStrongestNegative = (events) =>
  events
    .filter((event) => event.status === "success" && Number(event.car_value) < 0)
    .sort((a, b) => Number(a.car_value) - Number(b.car_value))[0];

const renderKpiCards = (events) => {
  const totalEvents = events.length;
  const successfulEvents = events.filter((event) => event.status === "success").length;
  const failedEvents = events.filter((event) => event.status === "failed").length;
  const strongestPositive = getStrongestPositive(events);
  const strongestNegative = getStrongestNegative(events);

  const cards = [
    {
      label: "Total Events",
      value: totalEvents,
      note: "Events included in dashboard_data.csv",
    },
    {
      label: "Successful Events",
      value: successfulEvents,
      note: "Processed by Repo 2 engine",
    },
    {
      label: "Failed Events",
      value: failedEvents,
      note: "Recorded without stopping the batch",
    },
    {
      label: "Strongest Positive",
      value: strongestPositive?.event_name ?? "N/A",
      note: strongestPositive ? formatPercent(strongestPositive.car_percent) : "",
    },
    {
      label: "Strongest Negative",
      value: strongestNegative?.event_name ?? "N/A",
      note: strongestNegative ? formatPercent(strongestNegative.car_percent) : "",
    },
    {
      label: "Dashboard Status",
      value: "V1",
      note: "Deterministic intelligence layer",
    },
  ];

  document.getElementById("kpiCards").innerHTML = cards
    .map(
      (card) => `
        <div class="kpi-card">
          <p class="kpi-label">${card.label}</p>
          <p class="kpi-value">${card.value}</p>
          <p class="kpi-note">${card.note}</p>
        </div>
      `,
    )
    .join("");
};

const renderLatestEvent = (events) => {
  const sortedEvents = [...events].sort(
    (a, b) => new Date(b.event_date) - new Date(a.event_date),
  );
  const latestEvent = sortedEvents[0];
  if (!latestEvent) return;

  document.getElementById("latestEventTitle").textContent = latestEvent.event_name;
  const directionClass = `direction-${latestEvent.car_direction.toLowerCase()}`;
  const details = [
    ["Event Date", latestEvent.event_date],
    ["Mechanism", latestEvent.mechanism],
    ["Event Type", latestEvent.event_type],
    ["Asset / Benchmark", `${latestEvent.asset} / ${latestEvent.benchmark}`],
    ["CAR Percent", formatPercent(latestEvent.car_percent)],
    [
      "CAR Direction",
      `<span class="${directionClass}">${latestEvent.car_direction}</span>`,
    ],
    ["Status", latestEvent.status],
    ["Report", latestEvent.report_path],
  ];

  document.getElementById("latestEventDetails").innerHTML = details
    .map(
      ([label, value]) => `
        <div class="detail-item">
          <p class="detail-label">${label}</p>
          <p class="detail-value">${value}</p>
        </div>
      `,
    )
    .join("");
};

const renderMarkdown = (markdown) => {
  const lines = markdown.split(/\r?\n/);
  let html = "";
  let inList = false;
  let inTable = false;
  let tableRows = [];

  const closeList = () => {
    if (inList) {
      html += "</ul>";
      inList = false;
    }
  };

  const closeTable = () => {
    if (!inTable) return;
    const [header, separator, ...body] = tableRows;
    const headerCells = header
      .split("|")
      .filter(Boolean)
      .map((cell) => `<th>${cell.trim()}</th>`)
      .join("");
    const bodyRows = body
      .filter((row) => row !== separator)
      .map((row) => {
        const cells = row
          .split("|")
          .filter(Boolean)
          .map((cell) => `<td>${cell.trim()}</td>`)
          .join("");
        return `<tr>${cells}</tr>`;
      })
      .join("");
    html += `<table><thead><tr>${headerCells}</tr></thead><tbody>${bodyRows}</tbody></table>`;
    tableRows = [];
    inTable = false;
  };

  lines.forEach((line) => {
    if (line.startsWith("|")) {
      closeList();
      inTable = true;
      tableRows.push(line);
      return;
    }

    closeTable();

    if (line.startsWith("# ")) {
      closeList();
      html += `<h1>${line.replace("# ", "")}</h1>`;
    } else if (line.startsWith("## ")) {
      closeList();
      html += `<h2>${line.replace("## ", "")}</h2>`;
    } else if (line.startsWith("- ")) {
      if (!inList) {
        html += "<ul>";
        inList = true;
      }
      html += `<li>${line.replace("- ", "")}</li>`;
    } else if (line.trim()) {
      closeList();
      html += `<p>${line}</p>`;
    }
  });

  closeList();
  closeTable();
  return html;
};

const renderInsights = (insightData) => {
  const insightCards = document.getElementById("insightCards");
  const insights = insightData.insights ?? [];

  if (!insights.length) {
    insightCards.innerHTML =
      '<div class="insight-card"><p class="insight-title">No rule-based insights generated.</p></div>';
    return;
  }

  insightCards.innerHTML = insights
    .map(
      (insight) => `
        <article class="insight-card">
          <p class="insight-category">${insight.category}</p>
          <h3>${insight.title}</h3>
          <p class="insight-event">${insight.event_name} (${insight.event_id})</p>
          <p>${insight.explanation}</p>
          <dl class="evidence-list">
            <div>
              <dt>Rule</dt>
              <dd>${insight.evidence.rule}</dd>
            </div>
            <div>
              <dt>CAR</dt>
              <dd>${insight.evidence.car_percent}</dd>
            </div>
            ${
              insight.evidence.mechanism_mean_percent
                ? `<div><dt>Mechanism Avg.</dt><dd>${insight.evidence.mechanism_mean_percent}</dd></div>`
                : ""
            }
          </dl>
          <p class="insight-note">${insight.use_note}</p>
        </article>
      `,
    )
    .join("");
};

const renderContextSummary = (contextData) => {
  const runSummary = contextData.run_summary ?? {};
  const sourceFiles = contextData.source_files ?? [];
  const constraints = contextData.use_constraints ?? [];

  const items = [
    ["Events", runSummary.event_count ?? "N/A"],
    ["Successful", runSummary.successful_event_count ?? "N/A"],
    ["Failed", runSummary.failed_event_count ?? "N/A"],
    ["Sources", sourceFiles.join(", ")],
    ["Constraints", constraints.join("; ")],
    ["Purpose", contextData.purpose ?? "N/A"],
  ];

  document.getElementById("contextSummary").innerHTML = items
    .map(
      ([label, value]) => `
        <div class="detail-item">
          <p class="detail-label">${label}</p>
          <p class="detail-value">${value}</p>
        </div>
      `,
    )
    .join("");
};

const renderHistoricalComparison = (comparisonData) => {
  const comparisons = comparisonData.comparisons ?? [];
  const container = document.getElementById("historicalComparison");

  if (!comparisons.length) {
    container.innerHTML =
      '<div class="insight-card"><p>No historical comparisons available.</p></div>';
    return;
  }

  container.innerHTML = comparisons
    .map(
      (comparison) => `
        <article class="comparison-card">
          <p class="insight-category">${comparison.relative_strength}</p>
          <h3>${comparison.event_name}</h3>
          <dl class="evidence-list">
            <div>
              <dt>Event CAR</dt>
              <dd>${comparison.event_car_percent}</dd>
            </div>
            <div>
              <dt>Mechanism Avg.</dt>
              <dd>${comparison.mechanism_average_percent}</dd>
            </div>
            <div>
              <dt>Magnitude Ratio</dt>
              <dd>${
                comparison.magnitude_ratio === null
                  ? "N/A"
                  : Number(comparison.magnitude_ratio).toFixed(2)
              }</dd>
            </div>
          </dl>
          <p>${comparison.interpretation}</p>
        </article>
      `,
    )
    .join("");
};

const renderExecutiveBrief = (briefData) => {
  const mechanismSummaries = briefData.mechanism_summaries ?? [];
  const highlights = briefData.highlights ?? [];
  const comparisonSummary = briefData.comparison_summary ?? {};

  document.getElementById("executiveBrief").innerHTML = `
    <p>${briefData.overview}</p>
    <h3>Highlights</h3>
    <ul>
      ${highlights.map((highlight) => `<li>${highlight}</li>`).join("")}
    </ul>
    <h3>Mechanism Summaries</h3>
    <ul>
      ${mechanismSummaries
        .map((summary) => `<li>${summary.summary}</li>`)
        .join("")}
    </ul>
    <h3>Comparison Summary</h3>
    <p>
      ${comparisonSummary.comparison_count ?? 0} comparison(s);
      ${comparisonSummary.stronger_than_average_count ?? 0} stronger than average;
      ${comparisonSummary.weaker_than_average_count ?? 0} weaker than average.
    </p>
    <p class="insight-note">${briefData.analyst_note}</p>
    <p class="insight-note">${briefData.restriction_note}</p>
  `;
};

const loadDashboard = async () => {
  try {
    const [
      csvResponse,
      summaryResponse,
      insightsResponse,
      contextResponse,
      comparisonResponse,
      briefResponse,
    ] = await Promise.all([
      fetch(dashboardDataPath),
      fetch(executiveSummaryPath),
      fetch(eventInsightsPath),
      fetch(llmContextPath),
      fetch(historicalComparisonPath),
      fetch(executiveBriefPath),
    ]);

    if (
      !csvResponse.ok ||
      !summaryResponse.ok ||
      !insightsResponse.ok ||
      !contextResponse.ok ||
      !comparisonResponse.ok ||
      !briefResponse.ok
    ) {
      throw new Error("Unable to load Repo 2 dashboard outputs.");
    }

    const events = parseCsv(await csvResponse.text());
    const executiveSummary = await summaryResponse.text();
    const insightData = await insightsResponse.json();
    const contextData = await contextResponse.json();
    const comparisonData = await comparisonResponse.json();
    const briefData = await briefResponse.json();

    renderKpiCards(events);
    renderLatestEvent(events);
    document.getElementById("executiveSummary").innerHTML =
      renderMarkdown(executiveSummary);
    renderInsights(insightData);
    renderContextSummary(contextData);
    renderHistoricalComparison(comparisonData);
    renderExecutiveBrief(briefData);
  } catch (error) {
    document.getElementById("kpiCards").innerHTML =
      `<div class="kpi-card"><p class="kpi-value">Data unavailable</p><p class="kpi-note">${error.message}</p></div>`;
    document.getElementById("executiveSummary").textContent = error.message;
    document.getElementById("insightCards").textContent = error.message;
    document.getElementById("contextSummary").textContent = error.message;
    document.getElementById("historicalComparison").textContent = error.message;
    document.getElementById("executiveBrief").textContent = error.message;
  }
};

loadDashboard();
