## guisupport.rpy —— 精简版：仅保留 gui.scale（gui.rpy 各处 gui.scale(n) 依赖）。
## 模板后半段（gui7 生成器）只在 SDK launcher 存在，成品包必崩 ModuleNotFoundError，已剔除。
init -100 python in gui:

    def scale(n):
        return int(n)
