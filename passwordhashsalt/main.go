package main

import (
	"fmt"
	"log"

	"golang.org/x/crypto/bcrypt"
)

func main() {
	for {

		// Verwijzing naar de functie voor het opvragen van het userpassword en het generen van een salt.
		fmt.Println("\nEnter a password you want to secure:")
		pwd := getUserPWD()
		hash := hashAndSalt(pwd)

		// Wachtwoorden worden vergeleken daarom wordt de getUserPWD functie nog een keer aangeroepen.
		fmt.Println("\nEnter the password again:")
		pwd2 := getUserPWD()
		pwdMatch := comparePasswords(hash, pwd2)
		if pwdMatch == true {
			fmt.Println("Passwords does match.")
		} else {
			fmt.Println("Passwords doesn't match.")
		}
	}
}
func getUserPWD() []byte {
	var pwd string
	/* Onderstaande stukje heb ik geadviseerd gekregen via security om dat misschien te gebruiken.
	Het scant voor een user input en die stored die doormiddel van de pointer & in mijn eerder aangemaakte variabele pwd.
	_ is een 'blank identifier', hiervoor hoef je geen return value op te geven. De functie fmt.scan verwacht namelijk 2 variabele om te kunnen bepalen of er een error moet komen.
	Omdat ik die variabele verder niet nodig op het checken voor een error na gebruik ik een _ zodat ik er geen return valua aan mee hoef te geven.
	*/
	_, err := fmt.Scan(&pwd)
	if err != nil {
		log.Println(err)
		//log is een package die in een van de tutorials werd gebruikt die had gekeken, het geeft de tijd en datum aan voor het print commando.
		// Ik denk dat dat hier een toegevoegde waarde geeft als je dit op grotere schaal gaat toepassen daarom leek het mij leuk om te gebruiken.
	}
	//Return de pwd input als een byte dit is nodig omdat ik die later ga hashen, en als ik dit op deze manier doe hoef ik het later niet meer te converten.
	return []byte(pwd)
}
func hashAndSalt(pwd []byte) string {

	// Gebruik GenerateFromPassword uit de bcrypt package om het wachtwoord the hashen en te salten.
	// Meer uileg over deze functie vindt je in de readme.
	hash, err := bcrypt.GenerateFromPassword(pwd, 4)
	fmt.Println("The given password in bytes: ", pwd)
	fmt.Println("The given password hashed en salted: ")
	fmt.Println(hash)
	if err != nil {
		log.Println(err)
	}
	// return de hash als een string
	return string(hash)
}
func comparePasswords(hashedPwd string, normalPwd []byte) bool {
	//Vergelijk het hashed wachtwoord met het normale wachtwoord zonder hash.
	// Je krijgt het password als een string dus moet nog geconvert worden naar een byte.
	byteHash := []byte(hashedPwd)
	err := bcrypt.CompareHashAndPassword(byteHash, normalPwd)
	if err != nil {
		log.Println(err)
		return false
	}
	//als ze overeenkomen return true als dat niet is returned die false.
	return true
}
