install:
	@mkdir -p /usr/local/bin
	@mkdir -p /tmp/cfg/asm
	@chmod 777 /tmp/cfg/asm
	@cp ./src/main.py /usr/local/bin/cfg
