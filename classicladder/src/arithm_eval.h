
#define arithmtype int


int IdentifyVarIndexedOrNot(char * StartExpr,int * ResType,int * ResOffset, int * ResIndexType,int * ResIndexOffset);
int EvalCompare(char * CompareString);
void MakeCalc(char * CalcString,int VerifyMode);
arithmtype AddSub(void);
arithmtype Or(void);
char * VerifySyntaxForEvalCompare(char * StringToVerify, char ** ErrorAt);
char * VerifySyntaxForMakeCalc(char * StringToVerify, char ** ErrorAt);


