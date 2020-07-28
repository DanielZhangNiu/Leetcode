#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/syscall.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/time.h>

// check input params length and sign, and operation

int main(int argc, char ** argv)
{
    // return if the number of argument is less than 3
    if (argc < 3){
        printf("arguments not valid.\n");
        printf("usage: reserve cancel <number>.\n or: reserve set <number> <timespec> <timespec> <number>.\n");
        return 0;
    }
    // asssign the argv[1] to operator, which decide to call reserve or cancel
    char *operator = argv[1];
    if (strcmp(operator,"set")== 0){
        // if the opearation is reserve, but number of argument less than 6, return.
        if (argc != 6)
        {
            printf("arguments not valid.\n");
            printf("usage: reserve set <number> <timespec> <timespec> <number>.\n");
            return 0;
        }
        
        // asssign the argv[2] to be tid
        pid_t tid = atoi(argv[2]);
        if (tid < 0){
            printf("input not valid.\n");
            printf("The input tid should be positive.\n");
            return 0;
        }
        // assign the argv[3] to be C
        struct timespec *C, *T;
        long C_ms = atoi(argv[3]);
        C->tv_sec = C_ms / 1000;
        C->tv_nsec = (C_ms % 1000) * 1000000;
        
        
        // If the input C less than 0 or bigger than 60000, exit.
        if ( C_ms <= 0|| C_ms >60000)
        {
            printf("arguments not valid.\n");
            printf("The range of C should be 0 to 6000.\n");
            return 0;
        }
        // asssign the argv[4] to be T
        // If the input T less than 0 or bigger than 60000, exit.
        long T_ms = atoi(argv[4]);
        T->tv_sec = T_ms / 1000;
        T->tv_nsec = (T_ms % 1000) * 1000000;
        if (T_ms <= 0|| T_ms >60000)
        {
            printf("Input not valid.\n");
            printf("The range of T should be 0 to 6000.\n");
            return 0;
        }
        
        // asssign the argv[5] to be CPUid, it should be 1 ,2 ,3
        
        int CPUid = argv[5][0] - 48;
        
        if ((CPUid < 0|| CPUid > 3) || argv[5][1] != '\0')
        {
            printf("arguments not valid.\n");
            printf("The range of CPUid should be 0 to 3 integer.\n");
            return 0;
        }
        fprintf(stderr,"before syscall,tid: %d, cpu: %d.\n",tid,CPUid);
        long ressys = syscall(__NR_set_reserve, tid, C, T, CPUid);
        printf("return from syscall %ld",ressys);
        return 0;
        
    }else if (strcmp(operator,"cancel")== 0){
        if (argc != 3)
        {
            printf("arguments not valid.\n");
            printf("usage: reserve cancel <number>.\n");
            return 0;
        }
        pid_t tid= atoi(argv[2]);
        
        fprintf(stderr,"before syscall.\n");
        long rescancel = syscall(__NR_cancel_reserve, tid);
        printf("return from syscall %ld.\n",rescancel);
        
        return 0;
        
    }else{
        printf("arguments not valid.\n");
        printf("usage: reserve cancel <number>.\n or: reserve set <number> <timespec> <timespec> <number>.\n");
        return 0;
    }
}





public class RateLimiter {
    class Request{
        
    }
    class RequestWrapper {
        Request rq;
        int timestamp;
        public RequestWrapper(Request rq, int timestamp) {
            this.rq = rq;
            this.timestamp = timestamp;
        }
    }
    int limited;
    Map<String, Queue<RequestWrapper>> map;
    public RateLimiter() {
        limited = 50;
        map = new HashMap<String, Queue<RequestWrapper>>();
    }
    //每次进queue之前，把队列里过期的request wrapper出队（根据时间是否离现在时间超过一秒），然后查看当前queu的size是否超过50，不是的话，就选择进队
    public boolean shouldPrintMessage(Request rq, int timestamp, String ip) {
        RequestWrapper newrw = new RequestWrapper(rq, timestamp);
        if(!map.containsKey(ip)) {
            Queue q = new LinkedList<RequestWrapper>();
            q.offer(newrw);
            map.put(ip, q);
        } else {-baidu 1point3acres
            Queue q = map.get(ip);
            while(!q.isEmpty()) {
                RequestWrapper rw = (RequestWrapper) q.peek();
                if(rw.timestamp < timestamp) {
                    q.poll();
                }
            }
            if(q.size() >= limited) {
                return false; // or throw exception
            }
            q.offer(newrw);
            map.put(ip, q);
        }
        return true;
    }
}
