_FILES_CLASSICLADDER
_FILE-general.txt
PERIODIC_REFRESH=100
SIZE_NBR_RUNGS=100
SIZE_NBR_BITS=500
SIZE_NBR_WORDS=100
SIZE_NBR_TIMERS=10
SIZE_NBR_MONOSTABLES=10
SIZE_NBR_COUNTERS=10
SIZE_NBR_TIMERS_IEC=10
SIZE_NBR_PHYS_INPUTS=50
SIZE_NBR_PHYS_OUTPUTS=50
SIZE_NBR_ARITHM_EXPR=100
SIZE_NBR_SECTIONS=10
SIZE_NBR_SYMBOLS=100
_/FILE-general.txt
_FILE-timers.csv
; Timers :
; Base(see classicladder.h),Preset
2,5
1,5
2,5
1,10
1,10
1,10
1,10
1,10
1,10
1,10
_/FILE-timers.csv
_FILE-monostables.csv
; Monostables :
; Base(see classicladder.h),Preset
1,3
1,10
1,10
1,10
1,10
1,10
1,10
1,10
1,10
1,10
_/FILE-monostables.csv
_FILE-counters.csv
; Counters :
; Preset
0
0
0
0
0
0
0
0
0
0
_/FILE-counters.csv
_FILE-timers_iec.csv
; Timers IEC :
; Base(see classicladder.h),Preset,TimerMode(see classicladder.h)
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
_/FILE-timers_iec.csv
_FILE-arithmetic_expressions.csv
; Arithmetic expressions :
; Compare or Operate ones
@200/0@=1
@200/0@=2
@200/0@=3
@200/0@:=@200/0@+1
@200/0@>3
@200/0@:=1
@200/0@<1





























































































_/FILE-arithmetic_expressions.csv
_FILE-rung_0.csv
; Rung :
; all the blocks with the following format :
; type (see classicladder.h) - ConnectedWithTop - VarType (see classicladder.h) / VarOffset
#VER=2.0
#LABEL=
#COMMENT=parallel port inputs S4,S5,S6
#PREVRUNG=0
#NEXTRUNG=1
1-0-50/4 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 50-0-0/0
1-0-50/5 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 50-0-0/1
1-0-50/6 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 50-0-0/2
0-0-50/7 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/10
0-0-50/7 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/17
0-0-50/7 , 0-0-0/0 , 0-0-0/15 , 0-0-0/15 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/16
_/FILE-rung_0.csv
_FILE-rung_1.csv
; Rung :
; all the blocks with the following format :
; type (see classicladder.h) - ConnectedWithTop - VarType (see classicladder.h) / VarOffset
#VER=2.0
#LABEL=
#COMMENT=S7 or B20 for queue effect
#PREVRUNG=0
#NEXTRUNG=2
1-0-50/7 , 2-0-0/20 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 50-0-0/10
1-0-0/20 , 2-0-50/7 , 2-1-10/0 , 9-0-0/0 , 99-0-0/0 , 10-0-0/0 , 9-0-0/0 , 99-0-0/0 , 99-0-0/0 , 60-0-0/3
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 99-1-0/0 , 99-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
0-0-0/0 , 0-0-0/0 , 0-0-0/16 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/17
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
_/FILE-rung_1.csv
_FILE-rung_2.csv
; Rung :
; all the blocks with the following format :
; type (see classicladder.h) - ConnectedWithTop - VarType (see classicladder.h) / VarOffset
#VER=2.0
#LABEL=
#COMMENT=
#PREVRUNG=1
#NEXTRUNG=3
99-0-0/0 , 99-0-0/0 , 20-0-0/4 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 99-0-0/0 , 99-0-0/0 , 60-0-0/5
99-0-0/0 , 99-0-0/0 , 20-0-0/6 , 0-1-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
_/FILE-rung_2.csv
_FILE-rung_3.csv
; Rung :
; all the blocks with the following format :
; type (see classicladder.h) - ConnectedWithTop - VarType (see classicladder.h) / VarOffset
#VER=2.0
#LABEL=
#COMMENT=parallel outputs D0,D1,D2
#PREVRUNG=2
#NEXTRUNG=4
1-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 50-0-60/0
99-0-0/0 , 99-0-0/0 , 20-0-0/0 , 1-0-0/10 , 0-1-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-60/0
1-0-0/1 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 50-0-60/1
99-0-0/3 , 99-0-0/0 , 20-0-0/1 , 1-0-0/10 , 0-1-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-60/2
1-0-0/2 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 9-0-0/0 , 50-0-60/2
99-0-0/0 , 99-0-0/0 , 20-0-0/2 , 1-0-0/10 , 0-1-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
_/FILE-rung_3.csv
_FILE-sections.csv
; Sections
#VER=1.0
#NAME000=Prog1
000,0,-1,0,3,0
_/FILE-sections.csv
_FILE-sequential.csv
; Sequential
#VER=1.0
_/FILE-sequential.csv
_FILE-ioconf.csv
; I/O Configuration
0,0,0,889,0,8,1
1,0,0,888,0,8,0
_/FILE-ioconf.csv
_FILE-modbusioconf.csv
; Modbus Distributed I/O Configuration
_/FILE-modbusioconf.csv
_FILE-symbols.csv
; Symbols
#VER=1.0
_/FILE-symbols.csv
_/FILES_CLASSICLADDER
