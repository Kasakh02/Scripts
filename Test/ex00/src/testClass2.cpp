#include "../inc/testClass2.hpp"

testClass2::testClass2() {
	std::cout << "Default constructor called" << std::endl;
}

testClass2::~testClass2() {
	std::cout << "Default destructor called" << std::endl;
}

testClass2::testClass2(const testClass2& copy) {
	std::cout << "Default copy constructor called" << std::endl;
	*this = copy;
}

testClass2& testClass2::operator=(const testClass2& copy) {
	std::cout << "Default assignment operator called" << std::endl;
	(void)copy
}

