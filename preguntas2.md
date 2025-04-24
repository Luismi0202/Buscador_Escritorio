Criterio 6a) Objetivos estratégicos:
### ¿Qué objetivos estratégicos específicos de la empresa aborda tu software?

Mi software aborda la necesidad de optimizar la búsqueda de información en entornos laborales y educativos, reduciendo el tiempo necesario para acceder a datos relevantes. Esto se corresponde con los objetivos estratégicos de eficiencia operativa, mejora en la toma de decisiones y automatización de procesos manuales.

### ¿Cómo se alinea el software con la estrategia general de digitalización?

Se alinea con la estrategia de digitalización al centralizar las búsquedas en un solo sistema, integrando APIs externas (como SerpAPI) y proporcionando una interfaz accesible. Además, fomenta la transición hacia un manejo digital de los datos, haciendo que tengamos los mejores resultados al buscar sin tener que ir nosotros uno a uno viendo cuál de los resultados puede ser el más fiable o el que mejor dice las cosas, porque al final, no siempre el primer resultado será el mejor.

---

Criterio 6b) Áreas de negocio y comunicaciones:
### ¿Qué áreas de la empresa (producción, negocio, comunicaciones) se ven más beneficiadas con tu software?

Las áreas de producción (por ejemplo, soporte técnico para búsquedas rápidas de datos), negocio (investigación de mercado o análisis de la competencia) y comunicaciones (búsqueda de información relevante para marketing digital) se ven directamente beneficiadas.

### ¿Qué impacto operativo esperas en las operaciones diarias?

Espero un impacto positivo en la reducción de tiempos de búsqueda, una mejora en la productividad de los empleados y una mayor capacidad de respuesta ante consultas o problemas, especialmente en áreas de soporte y análisis. Además de comodidad a la hora de tener un buscador ideal a nuestro alcance con un solo clic en nuestros escritorios.

---

Criterio 6c) Áreas susceptibles de digitalización:
### ¿Qué áreas de la empresa son más susceptibles de ser digitalizadas con tu software?

- **Soporte técnico:** Automatización de consultas internas y externas.
- **Recursos humanos:** Búsqueda de información para análisis de perfiles o tendencias del mercado laboral.
- **Educación y formación:** Acceso rápido a materiales de referencia o investigaciones.

### ¿Cómo mejorará la digitalización las operaciones en esas áreas?

Mejorará las operaciones al reducir la dependencia de procesos manuales y facilitar el acceso a datos relevantes en tiempo real. Además, la integración con APIs externas permite obtener información actualizada y precisa.

---

Criterio 6d) Encaje de áreas digitalizadas (AD):
### ¿Cómo interactúan las áreas digitalizadas con las no digitalizadas?

Las áreas digitalizadas (como soporte técnico o análisis de datos) pueden servir como un puente para las no digitalizadas, proporcionando información procesada que puede ser utilizada manualmente. Por ejemplo, el historial de búsqueda almacenado en JSON puede ser compartido con áreas que aún no trabajan con herramientas digitales.

### ¿Qué soluciones o mejoras propondrías para integrar estas áreas?

Propondría la centralización de las búsquedas y resultados en una base de datos compartida, accesible tanto para áreas digitalizadas como no digitalizadas, garantizando una transición progresiva hacia una estrategia completamente digital.

---

Criterio 6e) Necesidades presentes y futuras:
### ¿Qué necesidades actuales de la empresa resuelve tu software?

Resuelve la necesidad de realizar búsquedas rápidas y centralizadas, manteniendo un historial accesible y gestionable. Esto es útil para empresas que necesitan información rápida para toma de decisiones y seguimiento de actividades.

---

Criterio 6f) Relación con tecnologías:
### ¿Qué tecnologías habilitadoras has empleado y cómo impactan en las áreas de la empresa?

- **SerpAPI:** Proporciona búsquedas avanzadas y precisas, facilitando el acceso a información de calidad.
- **Tkinter:** Ofrece una interfaz gráfica intuitiva, mejorando la experiencia de usuario y la adopción del software.
- **JSON:** Permite un almacenamiento ligero y eficiente del historial de búsquedas.

### Impacto:

Estas tecnologías reducen la complejidad de las búsquedas y hacen que el software sea fácil de usar y mantener.

### ¿Qué beneficios específicos aporta la implantación de estas tecnologías?

- Reducción del tiempo necesario para acceder a información relevante.
- Mayor facilidad de uso gracias a una interfaz gráfica simple.
- Capacidad de escalar el software para futuras integraciones, como almacenamiento en la nube.

---

Criterio 6g) Brechas de seguridad:
### ¿Qué posibles brechas de seguridad podrían surgir al implementar tu software?

Justamente me pasó en este proyecto de subir mi clave API sin querer, exponiéndola a todo el mundo, haciendo así que todos pudieran usarla para mandarle solicitudes a la API con mi clave. Es por esto que tuve que cambiarla a una nueva y volver a hacer un push para hacerla inutilizable.

También podría pasar que alguien robara de alguna forma el archivo JSON donde se guarda el historial del usuario y este se viera expuesto, mostrando todas sus búsquedas y sintiendo así que han invadido su privacidad.

### ¿Qué medidas concretas propondrías para mitigarlas?

- Se podría encriptar la clave API o hacer como he hecho yo, que es pedirla antes de ejecutar el programa. Así tendrás que funcionar con una clave que sea tuya (aunque bien es cierto que encriptarla quizás es lo más ideal, ya que así en cuanto ejecutas el programa no tienes que irte a SerpAPI y pedir la clave, sino que simplemente ejecutas y estás usando mi clave SerpAPI sin exponerla públicamente).
- También se podría buscar alguna forma de encriptar la información del historial para que solo se mostrara dentro del programa la información, pero que en el archivo JSON, su información esté encriptada. Así, si alguien lo roba de alguna manera, no podría entender el historial que está leyendo.

---

Criterio 6h) Tratamiento de datos y análisis:
### ¿Cómo se gestionan los datos en tu software y qué metodologías utilizas?

Los datos (historial de búsquedas) se almacenan en formato JSON, lo que permite una gestión ligera y estructurada. Se realizan validaciones para garantizar que los datos ingresados sean coherentes y útiles antes de ser almacenados.

### ¿Qué haces para garantizar la calidad y consistencia de los datos?

- Evito duplicados en el historial, moviendo búsquedas repetidas al inicio.
- Valido los resultados de la API antes de mostrarlos o almacenarlos.
- Ofrezco opciones de limpieza del historial para mantenerlo organizado y relevante.