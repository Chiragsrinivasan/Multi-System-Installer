import paramiko
import database


class remoteSystem:
    def __init__(self, softwareRepository : tuple, hostName : str, portNumber : str, userName : int, path : str, password : str) -> None:
        self.hostName = hostName
        self.userName = userName
        self.portNumber = portNumber
        self.password = password
        self.remotePath = path
        self.softwareRepo = softwareRepository
        self.hostpath = r'C:\Users\LENOVO\Desktop\final'
        self.softwareRepo.append(self.hostpath)
        
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=self.hostName, port=self.portNumber, username=self.userName, password=self.password)  

    def file_transfer(self, fileName : str) -> None:
        hostName, username, password, hostPath = self.softwareRepo
        cmd = f"sshpass -p {password} scp {username}@{hostName}:{hostPath}{fileName} {self.remotePath}"
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(cmd)
        except Exception as e:
            print("Exception: ", e)     

    def install_software(self, fileName : str) -> str:
        self.file_transfer(fileName)
        cmd = f'echo {self.password} | sudo -S apt install ./{fileName}'
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(cmd)
        except Exception as e:
            print("Exception: ", e)
        return stdout.read().decode("utf-8")

    def close_connection(self) -> None:
        self.ssh_client.close()          