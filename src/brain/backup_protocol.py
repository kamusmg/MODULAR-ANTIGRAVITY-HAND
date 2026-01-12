import shutil
import datetime
import os

def create_backup():
    # Configuration
    SOURCE_DIR = os.path.join(os.getcwd(), 'src')
    BACKUP_ROOT = os.path.join(os.getcwd(), 'backups')
    
    # Ensure backup dir exists
    if not os.path.exists(BACKUP_ROOT):
        os.makedirs(BACKUP_ROOT)
        print(f"[BACKUP] Created backup root: {BACKUP_ROOT}")
    
    # Generate Timestamped Filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"nucleus_core_backup_{timestamp}"
    backup_path = os.path.join(BACKUP_ROOT, backup_name)
    
    print(f"[BACKUP] Initiating Protocol...")
    print(f"   Source: {SOURCE_DIR}")
    print(f"   Target: {backup_path}.zip")
    
    try:
        shutil.make_archive(backup_path, 'zip', SOURCE_DIR)
        print(f"[BACKUP] SUCCESS. Core logic preserved.")
        print(f"[BACKUP] Location: {backup_path}.zip")
        return True
    except Exception as e:
        print(f"[BACKUP] CRITICAL ERROR: {e}")
        return False

if __name__ == "__main__":
    create_backup()
