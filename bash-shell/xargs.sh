cat ./mn_lost_20200524.log | awk -F ':' '{print $1}' | xargs -n1 -I {} cp {} /home/RAID0_PRO/cimiss_BCCD/A/A.0001.0028.R001


