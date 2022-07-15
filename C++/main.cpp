//
//  main.cpp
//  project_euler
//
//  Created by Ronny Steinke on 26.06.22.
//

#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <chrono>
#include "BigInt.hpp"
#include <algorithm>
#include <set>
#include <map>
#include <iostream>
#include <fstream>

using namespace std::chrono;

// functions used in some of the tasks

int sums(int n){
    int res = 0;
    for (int i = n; i > 0; i--) res+=i;
    return res;
}
long long productme(long long n){
    // max value 25 after that we need BigInt
    long long a = 1;
    for (auto i = n; i > 1; i--)a *=i;
    return a;
}

std::vector<int> primesfrom2toN(int N){
    
    // not a vector but a bool array
    // upper Limit atm 8_340_000
    bool vector1[N];
    memset(vector1, true, sizeof(vector1));
    
    int nmax = sqrt(N)+1;
    vector1[0] = 0;
    vector1[1] = 0;
    
    // crossing out all even numbers starting with 4 as 2 is a prime
    for (int x = 4; x <= N; x += 2) vector1[x] = 0;
    
    //crossing out multiples of primes
    for (int i = 3; i <= nmax; i+=2){
        if (vector1[i] == 1){
            for (int x = i*2; x <= N; x += i) vector1[x] = 0;
        }
    }
    
    // initalizing an array of size N that will contain the primes
    static int primes2[8340000];
    
    
    //std::vector<int> primes2(N/2,0);
    int count = 0;
    for (int i = 0; i <= N; i++){
        if  (vector1[i]){
            primes2[count] = i;
            count++;
        }
    }
    
    //putting all primes into a vector
    std::vector<int> primes(primes2,primes2 + count);
    return primes;
    //return std::vector<int>(primes2.begin(), primes2.begin() + count);;
}

bool isPrime(long int n){
    if (n == 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for(auto i = 3; i < sqrt(n)+1; i+=2){
        if (n % i == 0) return false;
    }
    return true;
}

std::vector<int> primesfrom2to100mio(int N){
    
    // a bool array
    static bool vector1[100000000];
    memset(vector1, true, sizeof(vector1));
    
    int nmax = sqrt(N)+1;
    vector1[0] = 0;
    vector1[1] = 0;
    
    // crossing out all even numbers starting with 4 as 2 is a prime
    for (int x = 4; x <= N; x += 2) vector1[x] = 0;
    
    //crossing out multiples of primes
    for (int i = 3; i <= nmax; i+=2){
        if (vector1[i] == 1){
            for (int x = i*2; x <= N; x += i) vector1[x] = 0;
        }
    }
    
    // initalizing an array of size N that will contain the primes
    static int primes2[50000000];
    
    
    //std::vector<int> primes2(N/2,0);
    int count = 0;
    for (int i = 0; i <= N; i++){
        if  (vector1[i]){
            primes2[count] = i;
            count++;
        }
    }
    
    //putting all primes into a vector
    std::vector<int> primes(primes2,primes2 + count);
    return primes;
    //return std::vector<int>(primes2.begin(), primes2.begin() + count);;
}


std::vector<int> primesfrom2toN_OLD(int N){
    
    std::vector<int> vector1 (N, 1);
    std::vector<int> primes;
    
    int nmax = sqrt(N)+1;
    vector1[0] = 0;
    vector1[1] = 0;
    
    // crossing out all even numbers starting with 4 as 2 is a prime
    for (int x = 4; x <= N; x += 2){
        vector1[x] = 0;
    }
    
    for (int i = 3; i <= nmax; i+=2){
        if (vector1[i] == 1){
            for (int x = i*2; x <= N; x += i){
                vector1[x] = 0;
            }
        }
    }
    
    for (int i = 0; i <= N; i++){
        if  (vector1[i] == 1){
            primes.push_back(i);
    }}
    return primes;
}

void TestingBigInt(){
    //BigInteger included from faheel.github.io/BigInt/
    BigInt big1 = 0,big2,big3;
    big2 = "123456789987654321";
    big3 = "123456789987654321";
    std::cout << big2 * big3 << "\n";
}

bool palindromchecker(std::string S){
    if (S.length() == 1){
        return true;
    }
    if (S.length() == 2){
        if (S[0] == S[1]){
            return true;
        }
        else{
            return false;
        }
    }
    if (S[0] == S[S.length()-1]){
        return palindromchecker(S.substr(1,S.length()-2));
    }
    return false;
}

std::vector<int> getfactors(int n){
    std::vector<int> factors;
    int nmax = sqrt(n) + 1;
    for (int i = 1;i <= nmax;i++){
        if (n % i == 0){
            factors.push_back(n/i);
            if (n/i == i) continue;
            factors.push_back(i);
        }
    }
    return factors;
}

bool isPenta(int n){
    int a = sqrt(1+(24*n));
    double b = sqrt(1+(24*n));
    if (a != b)return false;
    if (n > 0 and (1+(a)) % 6 == 0 ) return true;
    return false;
}


void printstr(std::string str1 ="", std::string str2 ="", std::string str3 ="",std::string str4 ="", std::string str5=""){
    //std::cout << str1 + " " + str2 + " " + str3 + " " + str4 + " " + str5 << std::endl;
    int c = 0;
    if(str1 != "") c++;
    if(str2 != "") c++;
    if(str3 != "") c++;
    if(str4 != "") c++;
    if(str5 != "") c++;
    
    switch(c)
    {
        case 0: std::cout << "No Input was given." << std::endl;break;
        case 1: std::cout << str1 << std::endl;break;
        case 2: std::cout << str1 << " " << str2 << std::endl;break;
        case 3: std::cout << str1 + " " + str2 + " " + str3 << std::endl;break;
        case 4: std::cout << str1 << " " << str2 << " " << str3 + " " + str4 << std::endl;break;
        case 5: std::cout << str1 << " " << str2 << " " << str3 + " " + str4 + " " + str5 << std::endl;break;
    }
}

void printint(int a){
    printstr(std::to_string(a));
}
void printlong(long long a){
    printstr(std::to_string(a));
}
void printchar(char c){
    std::cout << c << std::endl;
}

// *********************
// Solutions start here
// *********************


void Euler1() {
    int res = 0;
    for (int i = 1; i < 1000; i++){
        if (i % 5 == 0 or i % 3 == 0){
            res += i;
        }
    }
  std::cout << "EULER1:\n";
  std::cout << res << std::endl;
}

void Euler2() {
    int res = 0;
    int a = 1;
    int b = 1;
    
    for (int c = 0; c <= 4000000;){
        c = a + b;
        a = b;
        b = c;
        if (c % 2 == 0){
            res += c;
        }
    }
  std::cout << "EULER2:\n";
  std::cout << res << std::endl;
}


void Euler3() {
    int res = 0;
    int nmax = sqrt(600851475143);
    long long a = 600851475143;
    std::vector<int> primes = primesfrom2toN(nmax);
    for (int i:primes){
        if (a % i == 0){
            res = i;
        }
    }
    
  std::cout << "EULER3:\n";
  std::cout << res << std::endl;
}


void Euler4(){
    int res = 0;
    
    for(int a = 100; a < 1000; a++){
        for (int b = a+1; b < 1000; b++){
            int c = a*b;
            if (palindromchecker(std::to_string(c)) and c > res){
                res = c;
            }
        }
    }
    std::cout << res << std::endl;
}


void Euler5(){
    bool a = true;
    int i = 2520;
    while (a){
        i++;
        // 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
        // 16 -> 8,4,2         18 ->9,6,3          20 -> 10,5
        if (i % 16 == 0 and i % 18 == 0 and i % 20 == 0 and i % 12 == 0 and i % 7 == 0
            and i % 11 == 0 and i % 13 == 0 and i % 17 == 0 and i % 14 == 0 and i % 15 == 0
            and i % 19 == 0){
                std::cout << i << std::endl;
                a = false;
        }
    }
}


void Euler6(){
    int res1 = 0;
    int res2 = 0;
    
    for (int i = 0; i <= 100;i++){
        res1 += i*i;
        res2 += i;
    }
    std::cout << (res2*res2)-res1 << std::endl;
}


void Euler7(){
    std::vector<int> primes = primesfrom2toN(1000000);
    std::cout << primes[10000] << "\n";
}


void Euler8(){
    std::string a = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";

    long res = 0;

    for (int i = 0; i < 1000;i++){
        std::string b = a.substr(i,13);
        long temp = 1;
        for(char c : b) {
            int d = c - '0';
            temp *= d;
            }
        if (temp > res) res = temp;
        
    }
    std::cout << res << "\n";
}


void Euler9(){
    for (int a = 1; a < 500; a++){
        for(int b = a; b < 1000000; b++){
            double c = sqrt(a*a+b*b);
            int c2 = c;
            if ( c2 == c and a + b + c == 1000){
                std::cout << a << " "<<b<< " " <<c<< std::endl;
                std::cout << a*b*c2 << "\n";
                exit(0);
            }
        }
    }
}


void Euler10(){
    std::vector<int> primes = primesfrom2toN(2000000);
    long res = 0;
    for(int i : primes) res+=i;
    std::cout << res << "\n";
}


void Euler11(){
    int res = 0;
    int arr[20][20] =
        {{8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8},
        {49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0},
        {81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65},
        {52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91},
        {22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80},
        {24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50},
        {32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70},
        {67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21},
        {24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72},
        {21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95},
        {78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92},
        {16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57},
        {86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58},
        {19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40},
        {4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66},
        {88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69},
        {4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36},
        {20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16},
        {20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54},
        {1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48}};
    
    int temp1 = 0;
    int temp2 = 0;
    int temp3 = 0;
    int temp4 = 0;
    for (int a = 0; a < 16; a++){
        for (int i = 0; i < 16; i++){
            temp1 = arr[a][i] * arr[a][i+1] * arr[a][i+2] * arr[a][i+3];
            temp2 = arr[i][a] * arr[i+1][a] * arr[i+2][a] * arr[i+3][a];
            temp3 = arr[a][i] * arr[a+1][i+1] * arr[a+2][i+2] * arr[a+3][i+3];
            temp4 = arr[a][i+3] * arr[a+1][i+2] * arr[a+2][i+1] * arr[a+3][i];
            if (temp1 > res) res = temp1;
            if (temp2 > res) res = temp2;
            if (temp3 > res) res = temp3;
            if (temp4 > res) res = temp4;
        }}
    std::cout << res << "\n";
}

void Euler12(){
    int i = 1;
    int len = 0;
    int tri_num = 0;
    while (len < 500){
        tri_num += i;
        std::vector<int> a = getfactors(tri_num);
        len = int(a.size());
        i++;
    }
    std::cout << tri_num << "\n";
}

void Euler13(){
    //BigInteger included from faheel.github.io/BigInt/
    BigInt big0 = 0,big1,big2,big3,big4,big5,big6,big7,big8,big9,big10,big11,big12,big13,big14,big15,big16,big17,big18,big19,big20,big21,big22,big23,big24,big25,big26,big27,big28,big29,big30,big31,big32,big33,big34,big35,big36,big37,big38,big39,big40,big41,big42,big43,big44,big45,big46,big47,big48,big49,big50,big51,big52,big53,big54,big55,big56,big57,big58,big59,big60,big61,big62,big63,big64,big65,big66,big67,big68,big69,big70,big71,big72,big73,big74,big75,big76,big77,big78,big79,big80,big81,big82,big83,big84,big85,big86,big87,big88,big89,big90,big91,big92,big93,big94,big95,big96,big97,big98,big99,big100,res;
;
    big1 = "37107287533902102798797998220837590246510135740250";
    big2 = "46376937677490009712648124896970078050417018260538";
    big3 = "74324986199524741059474233309513058123726617309629";
    big4 = "91942213363574161572522430563301811072406154908250";
    big5 = "23067588207539346171171980310421047513778063246676";
    big6 = "89261670696623633820136378418383684178734361726757";
    big7 = "28112879812849979408065481931592621691275889832738";
    big8 = "44274228917432520321923589422876796487670272189318";
    big9 = "47451445736001306439091167216856844588711603153276";
    big10 = "70386486105843025439939619828917593665686757934951";
    big11 = "62176457141856560629502157223196586755079324193331";
    big12 = "64906352462741904929101432445813822663347944758178";
    big13 = "92575867718337217661963751590579239728245598838407";
    big14 = "58203565325359399008402633568948830189458628227828";
    big15 = "80181199384826282014278194139940567587151170094390";
    big16 = "35398664372827112653829987240784473053190104293586";
    big17 = "86515506006295864861532075273371959191420517255829";
    big18 = "71693888707715466499115593487603532921714970056938";
    big19 = "54370070576826684624621495650076471787294438377604";
    big20 = "53282654108756828443191190634694037855217779295145";
    big21 = "36123272525000296071075082563815656710885258350721";
    big22 = "45876576172410976447339110607218265236877223636045";
    big23 = "17423706905851860660448207621209813287860733969412";
    big24 = "81142660418086830619328460811191061556940512689692";
    big25 = "51934325451728388641918047049293215058642563049483";
    big26 = "62467221648435076201727918039944693004732956340691";
    big27 = "15732444386908125794514089057706229429197107928209";
    big28 = "55037687525678773091862540744969844508330393682126";
    big29 = "18336384825330154686196124348767681297534375946515";
    big30 = "80386287592878490201521685554828717201219257766954";
    big31 = "78182833757993103614740356856449095527097864797581";
    big32 = "16726320100436897842553539920931837441497806860984";
    big33 = "48403098129077791799088218795327364475675590848030";
    big34 = "87086987551392711854517078544161852424320693150332";
    big35 = "59959406895756536782107074926966537676326235447210";
    big36 = "69793950679652694742597709739166693763042633987085";
    big37 = "41052684708299085211399427365734116182760315001271";
    big38 = "65378607361501080857009149939512557028198746004375";
    big39 = "35829035317434717326932123578154982629742552737307";
    big40 = "94953759765105305946966067683156574377167401875275";
    big41 = "88902802571733229619176668713819931811048770190271";
    big42 = "25267680276078003013678680992525463401061632866526";
    big43 = "36270218540497705585629946580636237993140746255962";
    big44 = "24074486908231174977792365466257246923322810917141";
    big45 = "91430288197103288597806669760892938638285025333403";
    big46 = "34413065578016127815921815005561868836468420090470";
    big47 = "23053081172816430487623791969842487255036638784583";
    big48 = "11487696932154902810424020138335124462181441773470";
    big49 = "63783299490636259666498587618221225225512486764533";
    big50 = "67720186971698544312419572409913959008952310058822";
    big51 = "95548255300263520781532296796249481641953868218774";
    big52 = "76085327132285723110424803456124867697064507995236";
    big53 = "37774242535411291684276865538926205024910326572967";
    big54 = "23701913275725675285653248258265463092207058596522";
    big55 = "29798860272258331913126375147341994889534765745501";
    big56 = "18495701454879288984856827726077713721403798879715";
    big57 = "38298203783031473527721580348144513491373226651381";
    big58 = "34829543829199918180278916522431027392251122869539";
    big59 = "40957953066405232632538044100059654939159879593635";
    big60 = "29746152185502371307642255121183693803580388584903";
    big61 = "41698116222072977186158236678424689157993532961922";
    big62 = "62467957194401269043877107275048102390895523597457";
    big63 = "23189706772547915061505504953922979530901129967519";
    big64 = "86188088225875314529584099251203829009407770775672";
    big65 = "11306739708304724483816533873502340845647058077308";
    big66 = "82959174767140363198008187129011875491310547126581";
    big67 = "97623331044818386269515456334926366572897563400500";
    big68 = "42846280183517070527831839425882145521227251250327";
    big69 = "55121603546981200581762165212827652751691296897789";
    big70 = "32238195734329339946437501907836945765883352399886";
    big71 = "75506164965184775180738168837861091527357929701337";
    big72 = "62177842752192623401942399639168044983993173312731";
    big73 = "32924185707147349566916674687634660915035914677504";
    big74 = "99518671430235219628894890102423325116913619626622";
    big75 = "73267460800591547471830798392868535206946944540724";
    big76 = "76841822524674417161514036427982273348055556214818";
    big77 = "97142617910342598647204516893989422179826088076852";
    big78 = "87783646182799346313767754307809363333018982642090";
    big79 = "10848802521674670883215120185883543223812876952786";
    big80 = "71329612474782464538636993009049310363619763878039";
    big81 = "62184073572399794223406235393808339651327408011116";
    big82 = "66627891981488087797941876876144230030984490851411";
    big83 = "60661826293682836764744779239180335110989069790714";
    big84 = "85786944089552990653640447425576083659976645795096";
    big85 = "66024396409905389607120198219976047599490197230297";
    big86 = "64913982680032973156037120041377903785566085089252";
    big87 = "16730939319872750275468906903707539413042652315011";
    big88 = "94809377245048795150954100921645863754710598436791";
    big89 = "78639167021187492431995700641917969777599028300699";
    big90 = "15368713711936614952811305876380278410754449733078";
    big91 = "40789923115535562561142322423255033685442488917353";
    big92 = "44889911501440648020369068063960672322193204149535";
    big93 = "41503128880339536053299340368006977710650566631954";
    big94 = "81234880673210146739058568557934581403627822703280";
    big95 = "82616570773948327592232845941706525094512325230608";
    big96 = "22918802058777319719839450180888072429661980811197";
    big97 = "77158542502016545090413245809786882778948721859617";
    big98 = "72107838435069186155435662884062257473692284509516";
    big99 = "20849603980134001723930671666823555245252804609722";
    big100 = "53503534226472524250874054075591789781264330331690";
    res = big1+big2+big3+big4+big5+big6+big7+big8+big9+big10+big11+big12+big13+big14+big15+big16+big17+big18+big19+big20+big21+big22+big23+big24+big25+big26+big27+big28+big29+big30+big31+big32+big33+big34+big35+big36+big37+big38+big39+big40+big41+big42+big43+big44+big45+big46+big47+big48+big49+big50+big51+big52+big53+big54+big55+big56+big57+big58+big59+big60+big61+big62+big63+big64+big65+big66+big67+big68+big69+big70+big71+big72+big73+big74+big75+big76+big77+big78+big79+big80+big81+big82+big83+big84+big85+big86+big87+big88+big89+big90+big91+big92+big93+big94+big95+big96+big97+big98+big99+big100;
    
    std::string myres = res.to_string();
    std::cout << std::string(myres.begin(), myres.begin() + 10) << std::endl;
    //std::cout << myres[0] << "\n";
}

void Euler14(){
    // even n/2
    // odd (3*n)+1
    int res = 0;
    int res2 = 0;
    for (int i = 2; i < 1000000; i++){
        long long temp = i;
        int count = 0;
        while(temp != 1){
            if (temp % 2 == 0) temp = temp/2;
            else temp = (3*temp)+1;
            count++;
        }
        if (count > res) {
            res = count;
            res2 = i;
        }
    }
    std::cout << "\nMax-length: " << res+1 << "\nRes: " << res2 <<"\n";
}

void Euler15(){
    // formular = 2*n!/(n!+n!)
    BigInt a = 1,b = 1,res;
    for(int i = 2; i < 41; i++){
        if (i < 21) b *= i;
        a *= i;
    }
    res = a/(b*b);
    std::cout << res << std::endl;
}

void Euler16(){
    BigInt big1 = 2,big2;
    big2 = pow(big1, 1000);
    auto temp = big2.to_string();
    int res = 0;
    for  (auto f : temp) res += f - '0';
    std::cout << res <<"\n";;
}

void Euler17(){
    std::string nums_written[101] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twentyone", "twentytwo", "twentythree", "twentyfour", "twentyfive", "twentysix", "twentyseven", "twentyeight", "twentynine", "thirty", "thirtyone", "thirtytwo", "thirtythree", "thirtyfour", "thirtyfive", "thirtysix", "thirtyseven", "thirtyeight", "thirtynine", "forty", "fortyone", "fortytwo", "fortythree", "fortyfour", "fortyfive", "fortysix", "fortyseven", "fortyeight", "fortynine", "fifty", "fiftyone", "fiftytwo", "fiftythree", "fiftyfour", "fiftyfive", "fiftysix", "fiftyseven", "fiftyeight", "fiftynine", "sixty", "sixtyone", "sixtytwo", "sixtythree", "sixtyfour", "sixtyfive", "sixtysix", "sixtyseven", "sixtyeight", "sixtynine", "seventy", "seventyone", "seventytwo", "seventythree", "seventyfour", "seventyfive", "seventysix", "seventyseven", "seventyeight", "seventynine", "eighty", "eightyone", "eightytwo", "eightythree", "eightyfour", "eightyfive", "eightysix", "eightyseven", "eightyeight", "eightynine", "ninety", "ninetyone", "ninetytwo", "ninetythree", "ninetyfour", "ninetyfive", "ninetysix", "ninetyseven", "ninetyeight", "ninetynine", "onehundred"};
    int nums_length[101];
    for (int i = 0; i < 101;i++)nums_length[i] = int(nums_written[i].size());
        
    
    int count = 0;
    //for the answer to be correct we need to exclude zero
    for (int i = 1; i < 1001; i++){
        if (i < 100) count+=nums_length[i]*10;
        if (i == 100)count += 10; // len("onehundred")
        if (i == 200)count += 10; // len("twohundred")
        if (i == 300)count += 12; // len("threehundred")
        if (i == 400)count += 11;
        if (i == 500)count += 11;
        if (i == 600)count += 10;
        if (i == 700)count += 12;
        if (i == 800)count += 12;
        if (i == 900)count += 11;
        if (i == 1000)count += 11; // len("onethousand")
        if(i > 100 and i < 200)count += 13; //len("onehundredand")
        if(i > 200 and i < 300)count += 13; //len("twohundredand")
        if(i > 300 and i < 400)count += 15; //...
        if(i > 400 and i < 500)count += 14;
        if(i > 500 and i < 600)count += 14;
        if(i > 600 and i < 700)count += 13;
        if(i > 700 and i < 800)count += 15;
        if(i > 800 and i < 900)count += 15;
        if(i > 900 and i < 1000)count += 14;
    }
    printint(count);
}

void Euler18(){
    std::vector<std::vector<int>> vect = {{75},
        {95,64},
        {17,47,82},
        {18,35,87,1},
        {2,4,82,47,65},
        {19,1,23,75,3,34},
        {88,2,77,73,7,63,67},
        {99,65,4,28,6,16,7,92},
        {41,41,26,56,83,4,8,7,33},
        {41,48,72,33,47,32,37,16,94,29},
        {53,71,44,65,25,43,91,52,97,51,14},
        {7,11,33,28,77,73,17,78,39,68,17,57},
        {91,71,52,38,17,14,91,43,58,5,27,29,48},
        {63,66,4,68,89,53,67,3,73,16,69,87,4,31},
        {4,62,98,27,23,9,7,98,73,93,38,53,6,4,23}};
    
    for (int i = 13; i >= 0;i--){
        for (int x = 0; x < i+1;x++){
            int a = vect[i][x] + vect[i+1][x];
            int b = vect[i][x] + vect[i+1][x+1];
            if (a > b) vect[i][x] = a;
            else vect[i][x] = b;
        }}
   std::cout << ""  << vect[0][0] << std::endl;
}

void Euler19(){
    // 1904 == leap year
    // firsts: [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    // firsts in a leapyear: [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

    bool leapyear = false;
    int nmax = 0;
    int count = 0;

    // 1.1.1901 was tuesday
    int starting_day = 2; // 1 == monday, ... , 7 == sunday
    int day = starting_day;
    
    for (int i = 1901; i < 2001;i++){
        if (i%4 == 0){
            leapyear = true;
        }
        else leapyear = false;
        
        if (leapyear) nmax = 366;
        else nmax = 365;

        // the week day of 1.1. alters from year to year
        // var is updated at the end of each loop
        day = starting_day;
        
        for(int x = 0;x <= nmax; x++)
        {
            if(leapyear){ //the 1. occur on day 32, 61,92 and since we start counting with 0 its -1
                if (x == 0 or x == 31 or x == 60 or x == 91 or x == 121 or x == 152
                   or x == 182 or x == 213 or x == 244 or x == 274 or x == 306 or x == 335)
                {
                    if (day % 7 == 0)count++;
                }
            }
            else{
                if (x == 0 or x == 31 or x == 59 or x == 90 or x == 120 or x == 151
                 or x == 181 or x == 212 or x == 243 or x == 273 or x == 305 or x == 334)
                {
                    if (day % 7 == 0)count++;
                }
            }
                day++;
        }
        // if %7 == 0 it means its a sunday so we add 7
        // if %7 == 1 and we add 7 its still a monday
        starting_day = (day%7)+7;
    }
    printint(count);
}

void Euler20(){
    BigInt big1 = 1,big2;
    big2 = "1";
    int res = 0;
    for (int i = 1; i <= 100; i++){
        big1 = i;
        big2 *= big1;
    }
    std::string f = big2.to_string();
    for (auto c : f) res += c - '0';
    std::cout << res << "\n";
}

void Euler21(){
    int sum = 0;
    std::vector<int> pairs(10000,0);
    for(int x = 1; x < 10000; x++){
        int temp = 0;
        for(int i = 1; i < x;i++){
            if (x % i == 0) temp += i;
        }
        pairs[x] = temp;
        if (pairs[temp] == x and pairs[temp] != temp) sum += x + temp;
    }
    std::cout << sum << "\n";
}

void Euler22(){
    // apparently c++ reads the file char by char
    // so i put them all into a single string
    // i skipped the " and used the comas to reset word value
    long long res = 0;
    std::string temp = " ";
    std::fstream my_file;
        my_file.open("/Users/ronny/Documents/CPP/Euler/project_euler/project_euler/euler22", std::ios::in);
        if (!my_file) {
            std::cout << "No such file\n";
        }
        else {
            char ch;
            
            while (1) {
                if (my_file.eof()) break;
                my_file >> ch;
                if (ch == '"') continue;
                else temp += ch;
            }
        }
    my_file.close();
    

    std::vector<std::string> lol;
    std::string rofl;
    for (auto x : temp){
        if (x == ' ')continue;
        if (x == ',') {
            lol.push_back(rofl);
            rofl ="";
        }
        else rofl += x;
    }
    lol.push_back(rofl);
    std::sort(lol.begin(), lol.end());
    int counter = 0;
    for(auto x : lol){
        counter++;
        long long word_value = 0;
        for(auto c : x){
            word_value += c - 64;
        }
        res += (counter * word_value);
    }
    std::cout << res <<std::endl;
}


void Euler23(){
    int nmax = 28123;
    std::vector<int> issumofabundant(nmax, 0);
    std::vector<int> abundantnums;
    int res = 0;
    
    for (int i = 2; i < nmax; i++){
        int temp = 1;
        for (int x = i-1; x > 1; x--){
            if (i%x==0) temp += x;
        }
        if (temp > i) abundantnums.push_back(i);
    }
    
    for(int a : abundantnums){
        for(int b : abundantnums) issumofabundant[a+b] = 1;
    }
    
    for(int i = 1;i < nmax; i++){
        if (issumofabundant[i] == 0) res += i;
    }
    std::cout << res << "\n";
}


void Euler24(){
    std::string a = "0123456789";
    for (int i = 1; i < 1000000; i++) std::next_permutation(a.begin(),a.end());
    std::cout << a << "\n";
}


void Euler25(){
    BigInt fib1 = 1, fib2,fib3;
    fib2  = "1";
    fib3 = "2";
    int count = 3;
    while (fib3.to_string().size() < 1000){
        count++;
        fib1 = fib2;
        fib2 = fib3;
        fib3 = fib1 + fib2;
    }
    std::cout << count << "\n";
    
}

void Euler26(){
    // reoccuring  decimal digits
    int nmax = 1001,res_d=0;
    std::string res = "";
    for (int denominator = 0; denominator<nmax;denominator++)
    {
        int rem = 1 % denominator;
        std::set<int> ive_seen_this_before;
        std::string res_temp;
        while(rem != 0 and ive_seen_this_before.find(rem) == ive_seen_this_before.end())
        {
            ive_seen_this_before.insert(rem);
            rem *= 10;
            int temp = rem / denominator;
            res_temp += std::to_string(temp);
            rem = rem % denominator;
        }
        if (res_temp.size() > res.size())
        {
            res = res_temp;
            res_d = denominator;
        }
        res_temp = "";
    }
    printint(res_d);
}

void Euler27(){
    // n*n + n + 41
    int count = 0, res = 0,co1=0,co2=0;
    std::vector<int> primes = primesfrom2toN(1000);
    // when n == 0 ,x must be prime
    for (int x : primes){
        for(int y = -100; y < 0; y++){
            count = 0;
            for(int n = 0; n < 1000; n++){
                long a = (n*n) + (y*n) + x;
                if(a < 0 or isPrime(a) == false)break;
                count++;
            }
            if (count > res){
                res = count;
                co1 = y;
                co2 = x;
            }
        }
    }
    std::cout << "Coefficients: " <<co1<<" "<<co2 << std::endl;
    std::cout << "Result:       " << co1*co2 << "\n\n";
}

void Euler28(){
    /*
     43 44 45 46 47 48 49
     42 21 22 23 24 25 26
     41 20  7  8  9 10 27
     40 19  6  1  2 11 28
     39 18  5  4  3 12 29
     38 17 16 15 14 13 30
     37 36 35 34 33 32 31
     
     +2 (*4)   +4(*4) +6
     */
    auto temp = 1;
    auto res = 1;
    // i = 1 1x1 grid    i = 2   3*3 grid       i = 3 5*5 grid    i = 4 7*7 grid
    // 101 grid == i (1001-1) / 2
    for (int i = 1; i <= 500; i++ ){
        for(int x = 0; x < 4; x++){
            temp += (2*i);
            res += temp;
        }
        
    }
    std::cout << res << "\n";
}


void Euler29(){
    std::set<std::string> s1;
    BigInt big1;
    for (int i = 2; i <= 100; i++){
        for(int x = 2; x <= 100; x++){
            big1 = pow(std::to_string(i),x);
            s1.insert(big1.to_string());
        }
    }
    std::cout << s1.size() << std::endl;
}


void Euler30(){
    // 194979 last number
    // res = 443839
    auto res = 0;
    // debug bool booli = true;
    for(int i = 2; i < 250000; i++ ){
        std::string tempstring = std::to_string(i);
        int tempres = 0;
        for (auto c : tempstring){
            int a = c - '0';
            tempres += pow(a,5);
        }
        if (tempres == i) res += i;
    }
    std::cout << res <<"\n";
}


void Euler31(){
    //coin sums
    std::vector<int> ways (201,0);
    ways[0] = 1;
    std::vector<int> coins = {1,2,5,10,20,50,100,200};
    for(int x : coins){
        for(int i = 0; i <= 200-x; i++){
            ways[i+x] += ways[i];
        }
    }
    std::cout << ways[200] <<std::endl;
}


void Euler32(){
    /*
    std::string b = std::to_string(a);
    std::cout << b <<"\n";
    std::sort(b.begin(),b.end());
    std::cout << b <<"\n"; */
    
    std::string pandigital = "123456789";
    std::vector<bool> ispan (32000,false);
    
    int res = 0;
    for (int x = 1; x < 32000; x++){
        for (int y = 1; y < 32000; y++){
            std::string tempres = "";
            tempres += std::to_string(x) + std::to_string(y) + std::to_string(y*x);
            std::sort(tempres.begin(),tempres.end());
            if ( size(tempres) > 9) break;
            if (tempres == pandigital) ispan[x*y] = true;
        }
    }
    for (int i = 0; i < 32000; i++){
        if (ispan[i]) res += i;
    }
    std::cout << res << "\n";
}


void Euler33(){
    int res1 = 1, res2 = 1;
    for (int a = 0; a < 10; a++){
        for (int b = 0; b < 10; b++){
            if(a == 0 and b == 0)continue;
            for (int c = 0; c < 10; c++){
                if ((a == 0 and c == 0) or c == b)continue;
                // ba/ac == b/c
                std::string num_temp;
                std::string de_temp;
                num_temp = std::to_string(b) + std::to_string(a);
                de_temp = std::to_string(a) + std::to_string(c);
                double num = std::stod(num_temp);
                double de = std::stod(de_temp);
                double temp_res1 = num/de;
                double temp_res2 = double(b)/double(c);
                if (temp_res1 == temp_res2){
                    res1 *= b;
                    res2 *= c;
                }
            }
        }
    }
    printint(res2/res1);
}


void Euler34(){
    int res = 0;
    for (int i = 3; i<50000; i++){
    std::string temp = std::to_string(i);
    int tempres = 0;
    for(auto c : temp) {
        int d = c - '0';
        int tempres2 = 1;
        for(int x = d; x > 0; x--){
            tempres2 *= x;
            }
        tempres += tempres2;
        }
        if (tempres == i ) res += i;
    }
    std::cout << res << "\n";
}


void Euler35(){
    std::vector<int> primes = primesfrom2toN(1000000);
    // res = 1 because the prime 2 will be skipped due to even number check
    int res = 1;
    for (auto prime : primes){
        std::string rotated_prime, prime_as_string;
        prime_as_string = std::to_string(prime);
        std::vector<int> rotated_primes;
        auto len = size(prime_as_string);
        bool booli = false;
        
        // check if prime contains even number
        for (auto c : prime_as_string){
            int d = c - '0';
            if (d % 2 == 0){
                booli = true;
            }
        }
        // if yes we skip this number
        if (booli) {
            continue;
        }
        //rotating the prime
        for (int i = 0; i <= len; i++){
            rotated_prime = prime_as_string.substr(1) + prime_as_string[0];
            rotated_primes.push_back(std::stoi(rotated_prime));
            prime_as_string = rotated_prime;
        }
        
        int count = 0;
        for (int i : rotated_primes){
            if (isPrime(i)) count+= 1;
        }
        if (size(rotated_primes) == count) res += 1;
    }
    std::cout << res << "\n";
}

void Euler36(){
    int res = 0;
    
    for (int i = 1; i < 1000001;i++){
        std::string str = std::bitset<32>(i).to_string();
        std::string temp = "";
        bool booli = true;
        for (auto x:str){
            if (booli and (x == '0'))continue;
            if (x == '1') booli = false;
            temp += x;
        }
        if (palindromchecker(temp) and palindromchecker(std::to_string(i))){
            res+= i;
        }
    }
    printint(res);
}

void Euler37(){
    std::vector<int> primes = primesfrom2toN(1000000);
    std::string prime_as_string;
    int res = 0;
    for (int i = 4; i < size(primes);i++){
        prime_as_string = std::to_string(primes[i]);
        bool booli = true;
        
        for (int x = 1; x < size(prime_as_string);x++){
            int a = std::stoi(prime_as_string.substr(0,x));
            int b = std::stoi(prime_as_string.substr(x));
            if(isPrime(a) == 0 or isPrime(b) != 1) booli = false;
            }
        if (booli) {
            // std::cout << primes[i] << std::endl;
            res += primes[i];
        }
    }
    std::cout << res << "\n";
}

void Euler38(){
    std::string pand = "123456789";
    long res = 0;
    for (int i = 1; i < 10001;i++){
        std::string temp = "";
        for (int x = 1; x < 4;x++){
            temp += std::to_string(i*x);
            std::string temp2 = temp;
            std::sort(temp2.begin(),temp2.end());
            if (temp2 == pand and std::stoi(temp) > res) res = std::stoi(temp);
        }
    }
    printlong(res);
}

void Euler39(){
    int res = 0, res_p = 0,count = 0;
    for (int p = 2; p < 1001;p++){
         for(int a = 1; a < p; a++){
            for(int b = a+1; a+b < p; b++){
                double c = sqrt(a*a + b*b);
                if(c == int(c) and a+b+c == p)count++;
            }
         }
        if (count > res){
            res = count;
            res_p = p;
        }
        count = 0;
    }
    printstr(std::to_string(res),std::to_string(res_p));
}

void Euler40(){
    std::string str = "";
    int arr[7] = {1,10,100,1000,10000,100000,1000000};
    auto res = 1;
    int i = 0;
    while(size(str) < 1000001){
        str += std::to_string(i);
        i++;
    }
    for(int i:arr){
        res *= (str[i] - '0');
    }
    std::cout << res << "\n";
}

void Euler41(){
    //using prev permutation and exiting when finding one
    // only saves 1-4ms
    std::string arr[5] = {"54321","654321","7654321","87654321","987654321"};

    for (int i = 4; i >= 0;i--){
        // pas = prime as string
        std::string pas = arr[i];
        while (std::prev_permutation(pas.begin(), pas.end())){
            int a = std::stoi(pas);
            if (isPrime(a)){
                std::cout << a << std::endl;
                break;
            }
        }
    }
    
}


void Euler41_1st(){
    // using next permutation
    std::string arr[5] = {"12345","123456","1234567","12345678","123456789"};
    int res = 0;

    for (int i = 4; i >= 0;i--){
        // pas = prime as string
        std::string pas = arr[i];
        while (std::next_permutation(pas.begin(), pas.end())){
            int a = std::stoi(pas);
            if (isPrime(a) and a > res){
                res = a;
            }
        }
    }
    std::cout << res << std::endl;
}

void Euler42(){
    // apparently c++ reads the file char by char
    // so i put them all into a single string
    // i skipped the " and used the comas to reset word value
    int res = 0;
    std::string temp = " ";
    std::fstream my_file;
        my_file.open("euler42", std::ios::in);
        if (!my_file) {
            std::cout << "No such file\n";
        }
        else {
            char ch;
            
            while (1) {
                if (my_file.eof()) break;
                my_file >> ch;
                if (ch == '"') continue;
                else temp += ch;
            }
        }
    my_file.close();
    int x = 0;
    for(auto c : temp){
        if (c == ',' or c == ' '){
            double tri = 0;
            double n = 1;
            while (tri <= x){
                tri = (n/2)*(n+1);
                n++;
                if (tri == x)res+=1;
            }
            x = 0;
        }
        else x += c - 64;
    }
    std::cout << res <<std::endl;
}

void Euler43(){
    std::string z = "1023456789";
    long long res = 0;
    while(std::next_permutation(z.begin(),z.end())){
        /*454.499 millisecond ohne var initialisierung und sortiert von 2 oben nach 17 unten*/
        
        
        /*404.556 milliseconds*/
        if(std::stoi(z.substr(7,3)) % 17 != 0)continue;
        if(std::stoi(z.substr(6,3)) % 13 != 0) continue;
        if(std::stoi(z.substr(5,3)) % 11 != 0) continue;
        if(std::stoi(z.substr(4,3)) % 7 != 0) continue;
        if(std::stoi(z.substr(3,3)) % 5 != 0) continue;
        if(std::stoi(z.substr(2,3)) % 3 != 0 )continue;
        if(std::stoi(z.substr(1,3)) % 2 == 0) res += std::stol(z);
        /**/
        /*472.395 milliseconds
         int a,b,c,d,e,f,g;
        a = std::stoi(z.substr(1,3));
        if (a % 2 != 0)continue;
        b = std::stoi(z.substr(2,3));
        if(b % 3 != 0 )continue;
        c = std::stoi(z.substr(3,3));
        if(c % 5 != 0) continue;
        d = std::stoi(z.substr(4,3));
        if(d % 7 != 0) continue;
        e = std::stoi(z.substr(5,3));
        if(e % 11 != 0) continue;
        f = std::stoi(z.substr(6,3));
        if(f % 13 != 0) continue;
        g = std::stoi(z.substr(7,3));
        if(g % 17 == 0) res += std::stol(z);*/
         }
    std::cout<< res <<std::endl;
}

bool Euler44(){
    // Pn=n(3n−1)/2
    // (4n**2-1n)/2
    std::vector<int> pentas;
    for (int i = 2; i < 2500; i++){
        int a = (i*((3*i)-1))/2;
        pentas.push_back(a);
    }
    
    for(auto x: pentas){
        for(auto y: pentas){
            if (x <= y) continue;
            int a = x-y;
            int b = x+y;
            if (isPenta(a) and isPenta(b)){
                std::cout << a << " " << b <<  " "<< b-a << std::endl;
                return true;
            }
        }
    }
    return false;
}

void Euler45(){
    /*Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
     
     Triangle         Tn=n(n+1)/2         1, 3, 6, 10, 15, ...
     Pentagonal         Pn=n(3n−1)/2         1, 5, 12, 22, 35, ...
     Hexagonal         Hn=n(2n−1)         1, 6, 15, 28, 45, ...
     It can be verified that T285 = P165 = H143 = 40755.

     Find the next triangle number that is also pentagonal and hexagonal.*/
    
    // Tipp: Every hexagonal number is a triangular number
    
    long int a,b,count = 0, p = 166,h = 144;
    
    while (count != 1){
        a = h*(2*h-1);
        b = p*(3*p-1)/2;
        if (a > b) p++;
        if (a < b) h++;
        if(a == b){
            std::cout << a << std::endl;
            count++;
        }
    }
}

void Euler46(){
    int nmax = 10000;
    std::vector<bool> res(nmax,false);
    std::vector<int> primes = primesfrom2toN(nmax);
    res[0] = true; res[1] = true;
    
    for (int i : primes){
        for(int s = 0; s<100; s++){
            int a = i + 2*(s*s);
            if (a > nmax) break;
            res[a] = true;
        }
    }
    for(int i = 0; i < res.size()-1;i++){
        if (i%2 != 0 and res[i] == false) {
            std::cout << i << std::endl;
            break;
        }
    }
}

void Euler47(){
    std::vector<int> primes = primesfrom2toN(1000);
    // apparently 2^2 and 3^3 are "distinct prime factors" ...
    primes.insert(primes.begin()+1,4);
    primes.insert(primes.begin()+5,9);
    

    // saves possible results with their factors
    std::vector<std::vector<int>> factor_map;
    for (int a : primes){
        for (int b : primes){
            if(a >= b) continue;
            for (int c : primes){
                if(b >= c) continue;
                for (int d : primes){
                    if (a*b*c*d > 1000000)break;
                    if(c >= d) continue;
                    factor_map.push_back(std::vector<int> {a*b*c*d,a,b,c,d});
                }
            }
        }
    }

    // sorts the vectors by the first value
    std::sort(factor_map.begin(),factor_map.end());
    
    //check if the next 3 list items are bigger by 1 each
    for (int i = 0; i <= factor_map.size()-4; i++) {
        if (factor_map[i][0]+1 == factor_map[i+1][0] and
             factor_map[i][0]+2 == factor_map[i+2][0] and
              factor_map[i][0]+3 == factor_map[i+3][0]){
                std::set<int> temp_set;
            
            // if so, insert their factors into a set
            for (int x = 1; x < 5; x++){
                temp_set.insert(factor_map[i][x]);
                temp_set.insert(factor_map[i+1][x]);
                temp_set.insert(factor_map[i+2][x]);
                temp_set.insert(factor_map[i+3][x]);
            }
            // the set should contain now 16 distinct prime factors
            if (temp_set.size() == 16){
                printint(factor_map[i][0]);
                printint(factor_map[i+1][0]);
                printint(factor_map[i+2][0]);
                printint(factor_map[i+3][0]);
                break;
            }
            
        }
    }
}
    

void Euler48(){
    // super slow due to BigInt
    BigInt a = 0, b;
    for (int i = 1; i < 1001; i++){
        a = i;
        b += pow(a, i);
    }
    std::string c = b.to_string();
    for(auto i = c.size()-10;i <= c.size()-1;i++)std::cout << c[i];
    std::cout << std::endl;
}

void Euler49(){
    std::vector<int> primes = primesfrom2toN(10000);
    int count = 0;
    for (int i = 2; i < 5001; i+=2){
        if (count == 2)break;
        for(auto p:primes){
            if (p+i+i > 10000)break;
            if (isPrime(p+i) and isPrime(p+i+i)){
            std::string p1,p2,p3;
            p1 = std::to_string(p);
            p2 = std::to_string(p+i);
            p3 = std::to_string(p+i+i);
            std::sort(p1.begin(), p1.end());
            std::sort(p2.begin(), p2.end());
            std::sort(p3.begin(), p3.end());
                if (p1 == p2 and p2 == p3){
                    std::cout << p << " " << p+i << " " << p+i+i << "\n";
                    count++;
                    continue;
                }
            }
        }
    }
}

void Euler50(){
    int tempres = 0, count = 0, current_highest = 0, nmax = 1000000, res = 0;
    std::vector<int> primes = primesfrom2toN(nmax);
    for(int b = 0; b < size(primes); b++){
        tempres = 0;
        count = 0;
        for(int a = b; a < size(primes); a++){
            count += 1;
            tempres += primes[a];
            if (tempres > nmax) break;
            if(count > current_highest and isPrime(tempres)){
                current_highest = count;
                res = tempres;
            }
        }
    }
    std::cout << res << std::endl;
}


int main(int argc, const char * argv[]) {
    
    auto start = high_resolution_clock::now();
    Euler26(); // change number according to problem here
    auto stop = high_resolution_clock::now();
    
    // possible casts, seconds, milliseconds, microseconds, nanoseconds
    auto duration = duration_cast<microseconds>(stop - start);
    double time = duration.count();
    std::cout << "Computing Time: "
             << time/1000 << " milliseconds" << std::endl;
    return 0;
}
