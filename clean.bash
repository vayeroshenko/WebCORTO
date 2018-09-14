#!/bin/bash

########################################################################
#                                                                      #
# Copyright(C) 2017 - CORTO Collaboration                              #
# Thu Aug 31 15:46:54 CEST 2017                                        #
# Autor: Leonid Burmistrov                                             #
#                                                                      #
# Script description:                                                  #
#                     This script clean folder from *~ files           #
#                                                                      #
# Input paramete: NON                                                  #
#                                                                      #
#                                                                      #
# This software is provided "as is" without any warranty.              #
#                                                                      #
########################################################################

rm *~
rm ./WebCorto/*~
rm ./corto/*~
rm ./corto/migrations/*~
rm ./corto/templates/*~
rm ./corto/templates/corto/*~
