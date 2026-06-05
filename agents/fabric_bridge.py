import asyncio
import websockets
import json
import subprocess
import sys

GODOT_WS_URL = "ws://localhost:1058" # Standard port mapped in your Olodumare stack

async def stream_thermodynamics_to_godot():
    print("🚀 Fabric Bridge: Connecting to Olodumare Godot Server...")
    
    while True:
        try:
            async with websockets.connect(GODOT_WS_URL) as websocket:
                print("🔗 Fabric Bridge: Core connected to WebSocket layer.")
                
                # Launch the hardware engine script as a background subprocess
                # and capture its real-time print metrics line-by-line
                cmd = [sys.executable, "-u", "hardware/oshunmare_engine.py"]
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                
                print("🔥 Subprocess: Òṣùmàrè Engine ignited under Fabric supervision.")
                
                for line in iter(process.stdout.readline, ""):
                    line = line.strip()
                    # Look specifically for our localized calculation receipts
                    if "(Cooling Delta)" in line:
                        try:
                            # Extract the raw exponential scientific notation string
                            parts = line.split(":")
                            td_val = float(parts[1].split()[0])
                            
                            # Build the structural JSON payload
                            payload = {
                                "type": "thermodynamic_update",
                                "node": "Oshunmare",
                                "metric": "Td",
                                "value": td_val,
                                "timestamp": asyncio.get_event_loop().time()
                            }
                            
                            # Relay the token receipt straight into the virtual architecture
                            await websocket.send(json.dumps(payload))
                            print(f"📡 Fabric relayed receipt to Godot: {td_val:.5e} K")
                        except Exception as parse_err:
                            print(f"⚠️ Parsing issue: {parse_err}")
                            
                process.stdout.close()
                process.wait()
                
        except (websockets.exceptions.ConnectionClosed, ConnectionRefusedError):
            print("⏳ Godot server not reachable. Fabric retrying bridge link in 5 seconds...")
            await asyncio.sleep(5)

if __name__ == "__main__":
    try:
        asyncio.run(stream_thermodynamics_to_godot())
    except KeyboardInterrupt:
        print("\nStopping Fabric bridge layer gracefully.")
