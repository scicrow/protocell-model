run_var="RUN_prod.sh"
#Submit first run
jobid=$(sbatch --parsable --export=num1=1,num2=2 $run_var
echo "$jobid submitted"

#Submit dependencies
for i in {2..4}; do
    jobid=$(sbatch --parsable --export=num1=$i,num2=$[i+1] --dependency=afterok:$jobid $run_var)
    echo "$jobid submitted"
done
