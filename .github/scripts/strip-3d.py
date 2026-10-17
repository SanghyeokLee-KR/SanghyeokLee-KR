"""3D 잔디 그림(yoshi389111/github-profile-3d-contrib)에서 잔디만 남긴다.

도구에는 레이더 · 언어 원그래프 · 아래 숫자 줄을 끄는 설정이 없어서, 그림을 만든 뒤 지운다.
그림의 맨 위 자식 가운데 글자가 든 묶음(레이더, 원그래프, 숫자 줄)과 배경 사각형을 빼면
잔디만 남고 바탕은 투명해져 GitHub 라이트 · 다크 배경에 그대로 놓인다.
사용: python3 strip-3d.py <svg 파일>...
"""
import sys
import xml.etree.ElementTree as ET

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)

for path in sys.argv[1:]:
    tree = ET.parse(path)
    root = tree.getroot()
    removed = 0
    for child in list(root):
        tag = child.tag.split('}')[-1]
        is_bg = tag == 'rect' and 'fill-bg' in child.attrib.get('class', '')
        has_text = tag == 'g' and child.find(f'.//{{{NS}}}text') is not None
        if is_bg or has_text:
            root.remove(child)
            removed += 1
    tree.write(path, encoding='utf-8', xml_declaration=False)
    print(f'{path}: {removed}개 묶음 제거')
