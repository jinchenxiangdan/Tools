#include <iostream>
#include <unordered_map>
#include <openssl/sha.h>



std::unordered_map<std::string, std::string> MY_HASH_MAP;

std::string get_sha256(const std::string ) {

}

int main(int argc, char **argv) {
    using namespace std;
    



    return 0;
}

int add_to_hash_map(const std::string checksum, const std::string file_name) {
    // if find the checksum, it means we found duplicate files 
    if (MY_HASH_MAP.find(checksum) != MY_HASH_MAP.end()) {

    // else, we don't find the checksum it means no duplicate files 
    } else {
        
        MY_HASH_MAP[checksum] = file_name;
    }

}