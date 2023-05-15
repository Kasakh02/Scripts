#include "../inc/testClass3.hpp"

testClass3::testClass3() {
	std::cout << "Default constructor called" << std::endl;
}

testClass3::~testClass3() {
	std::cout << "Default destructor called" << std::endl;
}

testClass3::testClass3(const testClass3& copy) {
	std::cout << "Default copy constructor called" << std::endl;
	*this = copy;
}

testClass3& testClass3::operator=(const testClass3& copy) {
	std::cout << "Default assignment operator called" << std::endl;
	(void)copy
}

