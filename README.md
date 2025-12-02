# Ifá Virtual — Olodumare & Exu WebSocket Framework

[![Godot Engine](https://img.shields.io/badge/Godot-4.x-blue?logo=godot-engine&logoColor=white)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-brightgreen)]()

Ifá Virtual is a lightweight, extensible client/server networking framework built in **Godot 4**.

It consists of two fully independent Godot projects:

- **Olodumare** — the WebSocket **server**
- **Exu** — the WebSocket **client**

Running one server instance allows any number of Exu clients to connect.  
All clients receive messages broadcast by the server (“see-all, chat-to-all”).

This forms the foundation for future distributed simulations, virtual worlds, and larger systemic architectures.

---

## 📁 Project Structure

```
ifa-virtual/
├── Exu/            # Client project (Godot)
├── Olodumare/      # Server project (Godot)
└── docs/           # Architecture & protocol documents
```

---

## 🌍 Olodumare (Server)

- Built with `WebSocketServer`
- Handles multiple simultaneous clients
- Receives messages and multicasts them to all clients
- Intended to scale into a full authoritative networking layer

### Run the server:

1. Open `Olodumare/` in Godot 4
2. Run the main scene (`Olodumare.tscn`)
3. Default port: **8080**

---

## ⚡ Exu (Client)

- Uses `WebSocketClient`
- Connects to Olodumare
- Sends text or structured messages
- Receives all multicast messages from the server

### Run a client:

1. Open `Exu/` in Godot 4  
2. Run `Exu.tscn`  
3. Launch multiple instances to test multicasting

---

## 📡 Communication Protocol

A simple JSON message structure:

```json
{
  "sender": "client_id",
  "type": "chat",
  "payload": "Hello everyone!"
}
```

A full protocol specification is in:

➡️ `docs/protocol.md`

---

## 🚀 Installation

Clone via SSH:

```bash
git clone git@github.com:Boterick/ifa-virtual.git
```

Open each project independently in Godot.

---

## 🧱 Future Expansion

- Convert Exu + Olodumare into standalone **submodules**
- Expand WebSocket message types & metadata
- Add state replication for multiplayer scenes
- Integrate scripted message channels
- Connect to larger systemic/energy indexing models
- Build a VR-capable world on top

---

## 📚 Documentation

See the `/docs` folder:

- **architecture.md** — design overview  
- **protocol.md** — WebSocket message specification  

---

## 🤝 Contributing

Contributions are welcome.  
See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

---

## 📝 License

MIT License (recommended).
