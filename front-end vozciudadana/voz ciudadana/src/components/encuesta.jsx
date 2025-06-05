import React, { useState } from "react";

const encuesta = () => {
    const [respuesta, setRespuesta] = useState("");
    const [enviada, setEnviada] = useState(false);

    const handleChange = (e) => {
        setRespuesta(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setEnviada(true);
    };

    return (
        <div>
            <h2>Encuesta</h2>
            {!enviada ? (
                <form onSubmit={handleSubmit}>
                    <p>¿Estás de acuerdo con la propuesta?</p>
                    <label>
                        <input
                            type="radio"
                            name="respuesta"
                            value="Sí"
                            checked={respuesta === "Sí"}
                            onChange={handleChange}
                        />
                        Sí
                    </label>
                    <br />
                    <label>
                        <input
                            type="radio"
                            name="respuesta"
                            value="No"
                            checked={respuesta === "No"}
                            onChange={handleChange}
                        />
                        No
                    </label>
                    <br />
                    <label>
                        <input
                            type="radio"
                            name="respuesta"
                            value="Tal vez"
                            checked={respuesta === "Tal vez"}
                            onChange={handleChange}
                        />
                        Tal vez
                    </label>
                    <br />
                    <button type="submit" disabled={!respuesta}>
                        Enviar
                    </button>
                </form>
            ) : (
                <div>
                    <h3>¡Gracias por responder!</h3>
                    <p>Tu respuesta: <strong>{respuesta}</strong></p>
                </div>
            )}
        </div>
    );
};

export default encuesta;