package main

import (
	"fmt"
	"net"
	"strings"
)

func main() {
	fmt.Println("---- Network Interface Finder by Marijn  ----")

	//net.Interfaces is een standaard methode uit de net package. Deze leest al je netwerkinterfaces uit.
	ifaces, _ := net.Interfaces()
	for _, iface := range ifaces {
		fmt.Println("\nNetwork Interface:", iface)

		addrs, _ := iface.Addrs()
		for _, addr := range addrs {
			addrStr := addr.String()
			fmt.Println("    Network Adres: ", addr.Network(), addrStr)

			split := strings.Split(addrStr, "/")
			networkadres := split[0]

			//kijk wat voor soort ip adres het is.
			ip := net.ParseIP(networkadres)
			if ip.To4() != nil {
				fmt.Println("       ", networkadres, "is a ipv4 adres.")
			} else if ip.To16() != nil {
				fmt.Println("       ", networkadres, "is a ipv6 adres.")
			} else {
				fmt.Println("       ", networkadres, "is not a ipv4 adres or ipv6 adres.")
			}
			fmt.Println("       ", networkadres, "is interface-local multicast :", ip.IsInterfaceLocalMulticast())
			fmt.Println("       ", networkadres, "is link-local multicast      :", ip.IsLinkLocalMulticast())
			fmt.Println("       ", networkadres, "is link-local unicast        :", ip.IsLinkLocalUnicast())
			fmt.Println("       ", networkadres, "is global unicast            :", ip.IsGlobalUnicast())
			fmt.Println("       ", networkadres, "is multicast                 :", ip.IsMulticast())
			fmt.Println("       ", networkadres, "is loopback                  :", ip.IsLoopback())
		}
	}

}
