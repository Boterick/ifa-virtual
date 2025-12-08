 # Ifá Virtual — WebSocket Protocol Specification

This document defines the message structure used between Olodumare (server) and Exu (client).

---

## ✅ Overview

Messages are sent as **JSON strings**.  
All messages must include:  

- `type` — the message category  
- `sender` — unique identifier  
- `payload` — message content  

---

## 📨 Message Format

```json
{
  "type": "chat",
  "sender": "client_01",
  "payload": "Hello world!"
}
```

---

## 📚 Message Types

### **1. chat**
Used for general broadcast text.

```json
{
  "type": "chat",
  "sender": "client_05",
  "payload": "Good morning!"
}
```

### **2. system**
System-level notifications and events.

Examples:
- user joined  
- user disconnected  
- server startup  

```json
{
  "type": "system",
  "sender": "server",
  "payload": "client_07 joined the network"
}
```

### **3. future message types**
Planned:

- `state`  
- `command`  
- `event`  
- `sync`  

---

## 🔄 Message Flow

### **Client → Server**
- Client sends a chat or event message  
- Server receives and wraps it  

### **Server → All Clients**
- Server multicasts a unified message to **every client**, including the sender  

---

## 🔐 Future Extensions

- Digital signatures  
- Encrypted channels  
- Client authentication  
- Message versioning  

