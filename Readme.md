# Python – Mini Proyectos de Redes

Este repositorio contiene una colección de proyectos y ejemplos prácticos relacionados con redes en Python. Se exploran distintos modelos de comunicación entre procesos como TCP/UDP, RMI, RPC y patrones de comunicación como publicador/suscriptor.

---

## 🗂 Contenido

### 01 – Sockets Básico
- Ejemplo mínimo de comunicación cliente-servidor usando sockets TCP en Python.

### 02 – Chat UDP
- Implementación de chat entre dos usuarios usando protocolo UDP.

### 03 – Chat P2P
- Chat punto a punto (peer-to-peer) con sockets TCP bidireccionales.

### 04 – RPC
- Uso del módulo `xmlrpc.server` para crear un sistema RPC simple.

### 05 – RMI
- Simulación de llamadas remotas a métodos entre procesos con RPyC (o implementación propia).

### 06 – Sistema de Notificaciones (Pub/Sub con DB)
- Proyecto en el que un publicador puede registrar temas en una base de datos.
- Los suscriptores reciben notificaciones automáticamente cuando hay actualizaciones.
- Incluye persistencia, lógica de suscripción y uso de sockets.

---

## 🧪 Requisitos

```bash
python >= 3.8
