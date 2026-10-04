CXX ?= c++
CXXFLAGS ?= -std=c++20 -O2 -Wall -Wextra -Wpedantic -Werror

.PHONY: all check clean
all: build/spider-contracts
build/spider-contracts: tests/contracts.cpp $(wildcard include/spider/*.hpp)
	mkdir -p build
	$(CXX) $(CXXFLAGS) -Iinclude tests/contracts.cpp -o $@
check: build/spider-contracts
	python3 tools/check-foundation.py
	./build/spider-contracts
clean:
	rm -rf build
