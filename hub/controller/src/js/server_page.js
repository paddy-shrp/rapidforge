
function updateOperationsStatus(data) {
   if(data == null) return

   document.getElementById("website_status").innerText = (data["tapit-website"] ? "Running" : "Stopped")
   document.getElementById("proxy_status").innerText = (data["tapit-proxy"] ? "Running" : "Stopped")
   document.getElementById("dlogger_status").innerText = (data["tapit-dlogger"] ? "Running" : "Stopped")
   document.getElementById("internal_status").innerText = (data["tapit-internal"] ? "Running" : "Stopped")
}

function updateServerStatus(data) {
    if(data == null) return

    document.getElementById("cpu_status").innerText = "CPU (" + data["cpu"] + "%)"
    document.getElementById("memory_status").innerText = "MEMORY (" + data["memory"] + "%)"
    document.getElementById("disk_status").innerText = "DISK (" + data["disk"] + "%)"
}

function updateServerHistory(data) {
    timestamps = []
    cpu = []
    memory = []
    disk = []

    for(let datapoint of data) {
        timestamps.push(datapoint["timestamp"] * 1000)
        cpu.push(datapoint["cpu"])
        memory.push(datapoint["memory"])
        disk.push(datapoint["disk"])
    }

    plotValues("cpu_chart", timestamps, cpu)
    plotValues("memory_chart", timestamps, memory)
    plotValues("disk_chart", timestamps, disk)

}

function plotValues(elementID, timestamps, values) {

    var trace = {
      x: timestamps,
      y: values,
      mode: "lines",
      line: {
        shape: "hv",
        color: "rgb(55, 128, 191)",
        width: 2
      }
    };

    var data = [trace]

    averageValue = calculateAverage(values)

    var averageLine = {
      x: [timestamps[0], timestamps[timestamps.length - 1]],
      y: [averageValue, averageValue],
      mode: "lines",
      line: {
          color: "rgb(255, 99, 71)",
          width: 2,
          dash: "dot"
      }
    };

    if(averageValue != 0)
      data.push(averageLine)

    var annotation = {
      x: timestamps[timestamps.length - 1],
      y: averageValue,
      xref: "x",
      yref: "y",
      text: `${averageValue.toFixed(2)}`,
      showarrow: false,
      font: {
          color: "rgb(255, 99, 71)",
          size: 14
      },
      align: "left",
      xanchor: "left",
      yanchor: "middle"
    };

    var layout = {
      xaxis: {
        type: "date",
        tickformat: "%H:%M"
      },
      yaxis: {
        range: [0, 100]
      },
      showlegend: false,
      margin: {
        t: 50
      },
      annotations: [annotation]
    };

    Plotly.newPlot(elementID, data, layout, {displayModeBar: false});
}

function fetchOperationsData() {
    sendInternalRequest("operations/is_running").then(result => updateOperationsStatus(result))
}

function fetchServerData() {
    sendInternalRequest("data/system_info").then(result => updateServerStatus(result))
}

function fetchServerHistory() {
    sendInternalRequest("data/system_history").then(result => updateServerHistory(result))
}

window.onload = function() {
    fetchOperationsData()
    fetchServerData()
    fetchServerHistory()

    setInterval(fetchOperationsData, 500)
    setInterval(fetchServerData, 500)
    setInterval(fetchServerHistory, 5000)
}