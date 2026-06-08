# PyPI: Python Package Index (다른 사람들이 만들어 놓은 패키지들을 모아둔 외부 패키지 저장소) --> pypi.org
## - Python 패키지를 올리고 내려받는 공식 저장소

# pip: PyPI에서 패키지를 검색, 설치, 삭제하는 도구

# requirements.txt: 프로젝트에 필요한 패키지 목록을 적어두는 파일
# -> 해당 패키지 목록을 이용해서 일괄 설치가 가능.
# == 의존성 명세 파일 (의존 패키지 파일들을 명세함)


# requirements.txt 예시 내용
sample_requirements = """
# 웹 요청 라이브러리
requests==2.32.3

# 환경변수 파일(.env) 로딩
python-dotenv>=1.0.1

# 테스트 도구
pytest~=8.3.0
"""


pip_commands = [
    "python -m venv .venv",    # venv라는 이름의 가상환경 생성 (가상환경 폴더명 .venv)
    "source .venv\\Scripts\\activate",
    "python -m pip --version",
    "python -m pip install requests",   # requests 패키지 설치
    "python -m pip show requests",      # 설치된 request 패키지 정보 출력

    "python -m pip freeze > requirements.txt",      # 현재 가상환경 패키지 리스트를 파일 형태로 저장함 (freeze)!!!!!!!!!!!!

    "python -m pip install -r requirements.txt",    # -r: "읽어서"라는 의미 <--> -r이 없으면 읽지 않고 그 파일을 설치하려 함 --> 오류
    "python -m pip uninstall requests",
]

# 필수 패키지 목록
REQUIRED_PACKAGES = {
    "requests": "requests",
    "colorama": "colorama",
    "python-dotenv": "dotenv"
}

from importlib import import_module
from importlib.metadata import version, PackageNotFoundError
from io import StringIO

def find_missing_packages() -> list[str]:
    """ requirements.txt 작성된 패키지가 설치되어 있는지 확인 """

    missing_packages = [] # 설치 안 된 패키지를 저장할 list

    for package_name in REQUIRED_PACKAGES:
        try:
            # 패키지 버전 정보를 문자열로 반환
            # 단, 해당 패키지가 설치되어 있지 않으면 PackageNotFoundError 발생
            version(package_name)
        except PackageNotFoundError:
            missing_packages.append(package_name)

    return missing_packages

def print_installed_versions() -> None:
    """ 설치된 패키지 버전 출력(pip list) """
    for package_name in REQUIRED_PACKAGES:
        print(f"{package_name}=={version(package_name)}")

def print_import_results() -> None:
    """ 설치된 패키지를 실제 Python 모듈로 import 가능한지 확인 """
    for package_name, module_name in REQUIRED_PACKAGES.items():
        import_module(module_name) # 동적 import
        print(f"{package_name} -> {module_name} import 성공")


# 필수 패키지 중 설치되지 않은 패키지 list를 반환받아 저장
missing_packages = find_missing_packages()

if missing_packages:    # list에 값이 있으면 truthy하다.
    print("설치되지 않은 패키지:", missing_packages)

    for package_name in missing_packages:
        print(f"python -m pip install {package_name}")

else:                   # list에 값이 없으면 falsy하다.
    # print("requirements.txt")
    print("필수 패키지가 모두 설치되어 있습니다.")
    print_installed_versions()
    print_import_results()