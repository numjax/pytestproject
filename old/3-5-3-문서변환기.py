from abc import ABC, abstractmethod


class Document:
    def __init__(self, name, content):
        self._name = name
        self._content = content

    @property
    def content(self):
        """문서의 내용을 리턴한다"""
        return self._content

    def __str__(self):
        """문서의 정보를 문자열로 리턴한다"""
        return "문서 이름: {}\n문서 내용:\n{}".format(self._name, self._content)



class Exporter(ABC):
    @abstractmethod
    def export(self, new_name: str, document: Document):
        pass




class CSVExporter(Exporter):
    """문서를 csv 형식으로 변환하는 클래스"""

    def export(self, new_name, document):
        """문서를 변환한 후 주어진 이름으로 리턴한다"""
        print("\nCSV 파일로 변환 중~")

        new_content = document.content.replace("|", ",")
        exported_document = Document(new_name, new_content)

        print("변환 완료!\n")

        return exported_document


class HTMLExporter(Exporter):
    """문서를 HTML 형식으로 변환하는 클래스"""

    def export(self, new_name, document):
        """문서를 변환한 후 주어진 이름으로 리턴한다"""
        print("\nHTML 문서 변환 중~")

        new_content = """
<!DOCTYPE html>
<html>
<head>
<title>Title of the document</title>
</head>

<body>
{}
</body>

</html>
        """.format(document.content)
        exported_document = Document(new_name, new_content)

        print("변환 완료!\n")

        return exported_document


class ExportController:
    """문서를 특정 파일 형식으로 변환하는 클래스"""

    def __init__(self):
        self.exporter = None

    def set_exporter(self, exporter:Exporter):
        """변환하고 싶은 파일 타입에 맞는 변환기를 설정한다"""
        self.exporter = exporter

    def run_export(self, new_name, document):
        """파일을 변환해서 리턴한다"""
        if self.exporter is None:
            print("변환기를 정해주세요")
            return document

        return self.exporter.export(new_name, document)





# 변환기 컨트롤러 인스턴스 정의
export_handler = ExportController()



# csv 변환기 인스턴스, html 변환기 인스턴스 정의
csv_exporter = CSVExporter()
html_exporter = HTMLExporter()



# 변환할 문서 인스턴스 정의
document = Document(
    "직원정보.txt",
    """
이름|이메일
강영훈|younghoon@codeit.kr
이윤수|yoonsoo@codeit.kr
손동욱|dongwook@codeit.kr"""
)

# 기존 문서 출력
print(document)

# 변환기를 csv 변환기로 설정
export_handler.set_exporter(csv_exporter)

# 주어진 문서를 csv 문서로 변환
exported_document = export_handler.run_export("직원정보.csv", document)
# 변환된 문서 출력
print(exported_document)

export_handler.set_exporter(html_exporter)
exported_document = export_handler.run_export("직원정보.html", document)
print(exported_document)

print(CSVExporter.mro())
print(HTMLExporter.mro())




"""

현 과제에서는 Document 클래스는 실제로 구현이 된 클래스인 동시에 하위 모듈이고, 이걸 사용하는 상위 클래스, 
각 변환기 클래스들은 상위 모듈에 해당하는데요. 의존 관계 역전 원칙을 100% 따르는 코드를 작성하기 위해서는 
모든 상위와 하위 모듈의 관계 사이에는 추상화 레이어가 있어야 됩니다. 따라서 이 원칙을 100% 적용하기 위해서는 
말씀해주신 것과 같이 IDocument(또는 다른 이름의) 추상화 레이어를 추가해야 합니다.

의존 관계 역전 원칙을 정말 잘 이해하고 계신 것 같습니다!

토픽 초반 노트(https://www.codeit.kr/learn/courses/object-oriented-programming/2086)에서 언급됐던 
것과 같이, SOLID는 코드가 복잡해지고 거대해질수록 유지보수하기 쉽고, 견고한 코드를 쓰기 위해서 따르면 좋은 
원칙들입니다.

그러나 모든 코드가 100% SOLID 원칙을 따르는 것이 무조건적으로 좋다고 할 수 없으며, 오히려 간단한 코드가 작성하는데 
시간이 너무 많이 들거나, 이해하기 더 복잡해질 수도 있다고 했었는데요 (실제로 제품으로 사용되는 코드들 중 100% SOLID를 
따르는 코드는 존재하기 굉장히 힘듭니다).

프로그래밍을 할 때는 abstract pureness vs. code size vs. speed vs. efficiency 등 여러 가지 요소들이 
균형을 이루도록 코드를 작성합니다. 쉽게 생각하면, 코드를 작성할 때 생각해야되는 게 SOLID에서 강조하는 유지 
보수성과 견고함 뿐만 아니라, 코드가 얼마나 긴지, 다른 사람이 봤을 때 이해하기 쉬운지, 얼마나 빠르게 실행되는지, 
얼마나 효율적인지 (가장 직관적으로는 작성하는 거 및 실행도 빠르고 공간도 덜 차지하는) 등 많은 요소들을 생각해야 
된다는 말이죠. (다만 선택을 했을 때 뭘 잃고 뭘 얻는지 아는 실력이 있으면 더 좋겠죠?)

이걸 생각해봤을 때, 개인적으로는 의존 관계 역전 원칙을 100% 지키지 않아도 되는 경우는 이 두 가지 정도가 있을 거
 같은데요.

Document가 될 수 있는 클래스가 무조건 하나밖에 없을 때 (미래에도 다른 종류의 Document 클래스가 있을 가능성이 0%일 때)
Document가 될 수 있는 클래스가 엄청 많고 이 중 어떤 걸 사용해도 되긴 하지만 현재 특정 Document 클래스의 인스턴스를 
사용하는 게 무조건 더 효율적일 때 (여러 클래스들에서 사용하려는 기능은 똑같애도 알고리즘적으로 한 클래스를 사용하는 게 
무조건적으로 우월할 때)
지금 과제에서는 첫 번째 경우가 해당될 거 같습니다. Document 클래스가 딱 하나밖에 필요가 없고 과제 범위를 생각해봤을 
때 앞으로도 필요하지 않을 것을 100% 확신할 수 있기 때문에 굳이 Document 클래스 위에 추상화 레이어를 추가하지 않아도 
문제가 되지 않을 거 같습니다.

만약 이 과제가 아니라 훨씬 더 복잡하고 거대한 상업용 코드를 작성하고 있고, 여러 종류의 Document 클래스들이 있을 수 
있다면 말씀해주신 것과 같이 추상화 레이어를 넣는 게 좀 더 견고한 코드를 쓰는 것이겠죠.
"""