// Obtener el nombre del equipo desde la URL

const paramsHistograma = new URLSearchParams(window.location.search);
const nombreEquipoHistograma = paramsHistograma.get("nombre");

fetch(`http://localhost:5000/api/histograma/${nombreEquipoHistograma}`)
  .then(res => res.json())
  .then(data => {
    const cantidadesPorDia = Array(31).fill(0);
    data.forEach(e => {
      const dia = parseInt(e.dia);
      if (dia >= 1 && dia <= 31) {
        cantidadesPorDia[dia - 1] = e.cantidad;
      }
    });

    const ctx = document.getElementById("eventChart").getContext("2d");
    new Chart(ctx, {
      type: "bar",
      data: {
        labels: Array.from({ length: 31 }, (_, i) => i + 1),
        datasets: [
          {
            label: "Eventos por día",
            data: cantidadesPorDia,
            backgroundColor: "#ef5350",
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              stepSize: 1,
            },
          },
        },
      },
    });
  })
  .catch((error) => {
    console.error("❌ Error al cargar el histograma:", error);
  });
