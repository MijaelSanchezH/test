function cargarDatos(){
    //fetch("http://localhost:5000/api/equipos")
    fetch("/api/equipos")
        .then(response => response.json())
        .then(data => {
            const tabla = document.getElementById("tabla-equipos");
            tabla.innerHTML = ""; // Limpia la tabla antes de volver a llenar

            data.forEach(equipo => {
                const tr = document.createElement("tr");

                tr.innerHTML = `
                    <td>${equipo.sala}</td>
                    <td><a href="equipo.html?nombre=${equipo.nombre}">${equipo.nombre}</a></td>
                    <td>${equipo.temperatura}</td>  <!-- ESTA LÍNEA FALTABA -->
                    <td class="${
                        equipo.estado === 'Operativo' ? 'ok' : 
                        equipo.estado === 'Stand-by' ? 'sb' : 
                        equipo.estado === 'Alarma' ? 'fail' : ''
                    }">${equipo.estado}</td>
                `;
                tabla.appendChild(tr);
            });
    })
    .catch(err => {
        console.error("Error al obtener los datos del backend:", err);
    });
}

// Cargar por primera vez al iniciar la página
cargarDatos();

// Luego actualizar cada 5 segundos (5000 ms)
setInterval(cargarDatos, 5000);