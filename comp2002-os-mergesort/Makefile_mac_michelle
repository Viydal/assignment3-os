# Compiler (cc is clang on macOS, gcc/clang elsewhere)
CC := cc

# Compile flags (no libraries here)
CFLAGS := -Wall -Wpointer-arith -Wstrict-prototypes -std=gnu89 -fPIC -MMD -MP

# Linker libs/flags (put pthread here)
LDLIBS := -pthread

BIN  := test-mergesort
OBJS := test-mergesort.o mergesort.o

all: $(BIN)

$(BIN): $(OBJS)
	$(CC) -o $@ $^ $(LDLIBS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

.PHONY: clean
clean:
	/bin/rm -f $(BIN) $(OBJS) *.d

-include $(OBJS:.o=.d)
