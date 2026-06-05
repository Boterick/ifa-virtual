 # Ifá Virtual — Architecture Overview

This document describes the high-level architecture of the Olodumare (server) and Exu (client) systems.

---

## 🌍 System Overview

Ifá Virtual is a modular distributed system based on:

- **One server (Olodumare)** — authoritative messaging layer  
- **Many clients (Exu)** — lightweight user endpoints  
- **WebSocket communication** — real-time and bi-directional  

The framework is deliberately minimalist so it can expand into:

- VR worlds  
- simulations  
- distributed computation  
- multi-client orchestration  
- or larger systemic architectures  

---

## 🧠 Conceptual Roles

### **Olodumare (Server)**  
Serves as the “central consciousness” of the network:

- Accepts connections  
- Tracks clients  
- Receives messages  
- Multicasts messages to all clients  
- Ensures global consistency  

### **Exu (Client)**  
Acts as an “agent” in the distributed network:

- Connects to Olodumare  
- Sends local messages  
- Displays messages from other clients  
- Will later evolve into a full networked entity  

---

## 🔌 Communication Layer

The server and clients communicate over a WebSocket channel.

It supports:

- broadcast  
- direct messages (future)  
- structured messages  
- optional encryption layers (future)  

See `protocol.md` for detailed message structure.

---

## 🔧 Internal Godot Structure

Each Godot project has:

- `project.godot`  
- main scene (`Exu.tscn`, `Olodumare.tscn`)  
- main script (`Exu.gd`, `Olodumare.gd`)  

The system is designed to be clean, inspectable, and extendable.

---

## 🔮 Planned Enhancements

- Git submodules for Exu / Olodumare  
- VR support (OpenXR)  
- Multi-channel communication  
- Structured events (join/leave/state)  
- Stateful world replication  
- Authentication  
- Encrypted messaging  

