import numpy as np

def apply(temperature_list: list) -> dict:
    # numpyを利用する必要は無いが、サンプルとしてあえて利用する
    np_array = np.array(temperature_list)
    return {
        "mean": np_array.mean(axis=0), # 行の方向で計算
        "max": np_array.max(axis=0),
        "min": np_array.min(axis=0),
    }

# python -c "import weatherforecast as wf; wf.main()"
# python -c "import weatherforecast as wf; t=wf.get();r=wf.apply(t['temperature_2m']); print(r)"


