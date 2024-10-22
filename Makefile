# 定义变量
PROGRAM_NAME = elecmonitor

PYTHON_FILE = $(wildcard src/*.py)
DIST_DIR   = dist
BUILD_DIR  = build
ASSET_DIR   = assets

ASSET = $(wildcard $(ASSET_DIR)/*)

# 默认目标
all: exe

# 目标1: 使用pyinstaller生成exe文件
exe:
	.venv\Scripts\pyinstaller.exe --onefile --noconsole --name $(PROGRAM_NAME) $(PYTHON_FILE)
	cp $(ASSET) $(DIST_DIR)
	echo "项目文件已生成在$(DIST_DIR)目录下"

# 目标2: 清理生成的文件
clean:
	rm -rf $(DIST_DIR) $(BUILD_DIR)
	echo "已清理构建文件和目录"

# 帮助信息
help:
	echo "可用的目标:"
	echo "  make exe    # 使用pyinstaller生成exe"
	echo "  make clean  # 清理生成的文件和目录"

# 默认规则
.PHONY: exe clean help