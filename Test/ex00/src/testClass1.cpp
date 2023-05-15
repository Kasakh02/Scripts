#include "../inc/testClass1.hpp"

testClass1::testClass1() {
	std::cout << "Default constructor called" << std::endl;
}

testClass1::~testClass1() {
	std::cout << "Default destructor called" << std::endl;
}

testClass1::testClass1(const testClass1& copy) {
	std::cout << "Default copy constructor called" << std::endl;
	*this = copy;
}

testClass1& testClass1::operator=(const testClass1& copy) {
	std::cout << "Default assignment operator called" << std::endl;
	(void)copy
}

