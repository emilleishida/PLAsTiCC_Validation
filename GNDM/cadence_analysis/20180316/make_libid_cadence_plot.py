#!/usr/bin/env python
import sys
import os
import numpy as np
import astropy.table as at 
import matplotlib.pyplot as plt 


def main():
    d = at.Table.read('cadence_analysis_20180316_WFD.txt', format='ascii')
    pbs = ['u','g','r','i','z','Y']
    models = ['SN1a','RRLyrae']
    fields = ['1752','2150']
    fig1 = plt.figure(figsize=(15,10))
    fig2 = plt.figure(figsize=(15,10))
    bins = np.arange(0, 102., 2.)
    for i, pb in enumerate(pbs):
        labels1 = []
        labels2 = []
        ax1 = fig1.add_subplot(3,2,i+1)
        ax2 = fig2.add_subplot(3,2,i+1)
        d1 = []
        d2 = []
        for j, model in enumerate(models):
            ind1 = ((d['pb'] == pb) & (d['model'] == model) & (d['b'] < 0))
            ind2 = ((d['pb'] == pb) & (d['model'] == model) & (d['b'] > 0))
            label = '{}_{}_'.format(model, pb)
            label1 = label+fields[0]
            label2 = label+fields[1]
            labels1.append(label1)
            labels2.append(label2)
            c1 = d['cadence'][ind1]
            c2 = d['cadence'][ind2]
            d1.append(c1)
            d2.append(c2)
        ax1.hist(d1, bins=bins, histtype='bar', label=labels1)
        ax2.hist(d2, bins=bins, histtype='bar', label=labels2) 
        ax1.set_xlabel('{} Cadence (days)'.format(pb))
        ax1.set_ylabel('N')
        ax2.set_xlabel('{} Cadence (days)'.format(pb))
        ax2.set_ylabel('N')
        ax1.legend(frameon=False)
        ax2.legend(frameon=False)
    fig1.suptitle('LIBID 1752')
    fig2.suptitle('LIBID 2150')
    fig1.tight_layout(rect=[0, 0, 1, 0.93])
    fig2.tight_layout(rect=[0, 0, 1, 0.93])
    fig1.savefig('cadence_SN1a_RRLyrae_libid_1752.pdf')
    fig2.savefig('cadence_SN1a_RRLyrae_libid_2150.pdf')




if __name__=='__main__':
    sys.exit(main())
    plt.show(fig)




if __name__=='__main__':
    sys.exit(main())
