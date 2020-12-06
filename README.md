# robocopyList
파일 목록을 입력하여 해당 파일을 복사
톰캣(tomcat)에 배포(publish)된 파일 중 일부를 쉽게 추출하기 위해 만들어짐.

다음 특징을 제공
1. 디렉토리명 자동변환 \src\main\webapp -> (공백)
2. 디렉토리명 자동변환 \src\main\java -> \WEB-INF\classes
3. 디렉토리명 자동변환 \src\main\resources -> \WEB-INF\classes

사용방법
1. config.txt 파일을 열어 srcPath 복사하려는 파일이 있는 경로로 수정
2. filelist.txt 파일을 열어 srcPath 로부터 하위 경로를 입력. 여러줄로 다수 입력 가능
3. main.exe 실행
