'''
Created on May 14, 2012

This module reads a sdf file and a list of properties which need to be exported, it returns a table

@author: jshen @ NCTR, FDA
'''

import pybel as pb
import sys, getopt

def usage(name):
    print "\n"
    print "\tUSAGE\n"
    print "\t\t", name, "-i INPUTFILE -o OUTPUTFILE -p \"Properties\""
    print """
        PARAMETERS
        
            -h, --help    : Help
            -i,        : input sdf file, contain a list of mols
            -o,        : output file
            -p,        : properties need to be exported (delimited by ",")
        """
    sys.exit()

def mols2matrix(mols, props):
    matrix=[]
    matrix.append(props)
    #   print props

    ########Define the output sdf file####################
    outSDfile=pb.Outputfile("sdf","C:\Documents and Settings\jshen\My Documents\Research\EDKB\\toEPA\\NCTRlogRBA.sdf","overwrite=True")

    ##################################################


    # define an Pybel.Outputfile object to output sdf file

    for mol in mols:
        newmol=mol
        for key in mol.data.keys():
            if key not in props:
                del mol.data[key]

        ############select which should be output

        #if "NCTRlogRBA" in newmol.data.keys():
        if 1:
            outSDfile.write(newmol)
        ##########################################
        line=[]
        for prop in props:
            try:
                line.append(mol.data[prop])
            except:
                pass
        matrix.append(line)

    return matrix



if __name__ == '__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:p:",["help"])
    except getopt.GetoptError:
        usage(sys.argv[0])

    ###########define the input file#################
    propList="PK,CAS,Name,SMILES,ERlogRBA,NCTRlogRBA"
    infile="C:\Documents and Settings\jshen\My Documents\Research\EDKB\\toEPA\\ERcombine1086.sdf"
    outfile="C:\Documents and Settings\jshen\My Documents\Research\EDKB\\toEPA\\ERcombine1086.txt"



    ###############################################




    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage(sys.argv[0])
        elif opt in ("-i"):
            infile=arg
        elif opt in ("-o"):
            outfile=arg
        elif opt in ("-p"):
            propList=arg

    source="".join(args)
    props=propList.split(",")

    outp=open(outfile,"w")

    mols=list(pb.readfile("sdf", infile))

    outMatrix=mols2matrix(mols,props)

    for line in outMatrix:
        for item in line:
            outp.write("%s\t" % item)
        outp.write("\n")
    