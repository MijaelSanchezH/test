// Obtener el nombre del equipo desde la URL

const params = new URLSearchParams(window.location.search);
var nombre = params.get("nombre");

document.getElementById("titulo-equipo").textContent += nombre;

// Hacer petición al backend para obtener historial
//fetch(`http://localhost:5000/api/equipo/${nombre}`)
fetch(`/api/equipo/${nombre}`)
  .then(res => res.json())
  .then(data => {
    const historial = data.historial || [];
    const tabla = document.getElementById("tabla-historial");

    if (historial.length === 0) {
      tabla.innerHTML = `<tr><td colspan="3">No hay historial disponible.</td></tr>`;
    } else {
        console.log("📋 Historial recibido:", historial);
        historial.forEach(evento => {
            const tr = document.createElement("tr");

            tr.innerHTML = `
                <td>${evento.fecha}</td>
                <td>${evento.evento}</td>
                <td class="${evento.estado === 'Atendido' ? 'ok' : evento.estado === 'Stand-by' ? 'sb' : 'fail'}">${evento.estado}</td>
             `;

        tabla.appendChild(tr);
        });
    }
  })
  .catch(error => {
    console.error("Error al obtener el historial:", error);
  });