exit:
	@echo -e "\033[1;32mCommand needed: ...\n \ 
	 >>> make install"
	@exit 0

clean clear:
	@find . -name ".DS.Store" -delete
	@find . -name "__pycache__" -exec rm -rf {} +
	@find . -name ".vscode" -exec rm -rf {} +

start:
	@poetry run start
	@echo "All proxies found"
