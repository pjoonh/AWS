import asyncssh
import asyncio
import os

# SFTP 서버 정보 설정
SFTP_SERVER = 'xxx.xxx.xx.xx'
SFTP_PORT = xxxx
SFTP_USER = 'xxxxx'
SFTP_PASS = 'xxxxx'
REMOTE_PATH = 'xxxxxx'

# 업로드할 이미지 경로
IMAGE_PATH = "/home/aws2024/aws2024_code/aws2024_csv_data/temp_moist_graph.png"

# SFTP 업로드 함수 정의
async def upload_aws_image(image_path):
    try:
        # 원격 경로 설정
        remote_file_path = os.path.join(REMOTE_PATH, os.path.basename(image_path))

        async with asyncssh.connect(SFTP_SERVER, port=SFTP_PORT, username=SFTP_USER, password=SFTP_PASS) as conn:
            async with conn.start_sftp_client() as sftp:
                # 파일 업로드
                await sftp.put(image_path, remote_file_path)
                print(f"이미지가 성공적으로 업로드되었습니다: {remote_file_path}")

    except Exception as e:
        print(f"파일 업로드 중 오류 발생: {e}")

# 실행 함수 정의
def main():
    if os.path.exists(IMAGE_PATH):
        asyncio.run(upload_image(IMAGE_PATH))
    else:
        print("업로드하려는 이미지 파일이 존재하지 않습니다.")

# 이미지 업로드 실행
if __name__ == "__main__":
    main()
