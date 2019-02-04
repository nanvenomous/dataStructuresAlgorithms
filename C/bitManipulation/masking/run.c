#define VAR(vtype, memclass)  memclass vtype /* [COMPILER026] */

/* [PLATFORM013]          0 .. 255             */
typedef unsigned char uint8;
typedef unsigned short uint16; /* [PLATFORM014]          0 .. 65535           */ 
typedef unsigned long uint32;  /* [PLATFORM014]          0 .. 4294967295      */
/* [COMPILER046] [COMPILER036] Used for local non static variables */
#define AUTOMATIC

#define REG_BIT_CLEAR16(address, mask)    ((*(volatile uint16*)(address))&= (~(mask)))
#define ESCI_CR2_ADDR32(offset)    ((uint32)((uint32)( ESCI_au32BaseAddrs[(offset)]) + 0x04uL ))
#define ESCI_CR2_MDIS_MASK_U16               ((uint16)0x8000U)

void main() {
	VAR(uint8, AUTOMATIC) u8Lin_ESCI;
	REG_BIT_CLEAR16(ESCI_CR2_ADDR32(u8Lin_ESCI), ESCI_CR2_MDIS_MASK_U16);
}
