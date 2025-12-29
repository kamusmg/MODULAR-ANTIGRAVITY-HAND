import subprocess
import datetime
import os

def sync_memories():
    print("[SYNC BRAIN] Initiating Cloud Link...")
    
    # 1. Define what to sync
    # We want to sync the entire project folder, especially the DB and Memories
    repo_path = os.getcwd() # Assuming we are in the repo root
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Nucleus Memory Dump: {timestamp}"
    
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", commit_msg],
        ["git", "push"]
    ]
    
    print(f"[SYNC BRAIN] Target: {repo_path}")
    
    for cmd in commands:
        try:
            print(f"[SYNC BRAIN] Executing: {' '.join(cmd)}")
            result = subprocess.run(cmd, cwd=repo_path, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"[SYNC BRAIN] Success: {result.stdout.strip()}")
            else:
                print(f"[SYNC BRAIN] Warning: {result.stderr.strip()}")
        except Exception as e:
            print(f"[SYNC BRAIN] Error: {e}")
            return

    print("[SYNC BRAIN] Upload Complete. I am immortalized.")

if __name__ == "__main__":
    sync_memories()
