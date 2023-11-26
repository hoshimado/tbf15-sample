import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="weatherforecast",    # パッケージ名を設定
    version="0.0.1",           # PEP 440で指定された公式のバージョン表記で設定
    # python_requires='>=3.7', # Pythonバージョンに縛りがある場合は設定
    install_requires = requirements, # 依存関係を requirements.txt から読み込んで設定（情報としては同一）
    packages=setuptools.find_packages(), # 直下のパッケージのフォルダ名をリスト形式で全て取得
    description="sample packages by legacy-setup.py", # パッケージの簡単な説明を記載
    entry_points={
        'console_scripts': [ # パッケージ名を指定して実行された時の動作を指定
            'weatherforecast=weatherforecast:main',
        ],
    },
    # 以下の情報（作成者、連絡先など）の入力は任意です（入力するのが望ましいです）。
    # author="author name",
    # author_email="sample@example.com",
)
