python
AtraceMonitor
WatchdogMonitor
PlogFlush
adx_data_dump_t
PlogReportRecv
TraceClientRecv
MONITOR_0
REPORT_RAS
RT_RECYCLE
pt_autograd_*
VLLM::Worker
AOE_RTKB
CaffeTaskThread
hccl_watchdog_t
ZMQbg/Reaper
ZMQbg/IO/0
VLLM::Worker_DP
Hccl_HeartBeat
Hccl_ThrdManage
acl_thread
release_thread
sq_send_trigger_irq
cq_update_irq

线程类型	当前绑定	建议绑定	优先级
主计算线程（VLLM::Worker_DP）	[22-33]	[22-29]	最高
HCCL通信线程	[22-33]	[30-31]	高
PyTorch autograd线程	[22-33]	[32-33]	中
监控/日志线程	[22-33]	[40-43]	低
ZMQ后台线程	[22-33]	[44-45]	低
ACL线程	[34]	[34]	中
Release线程	[35]	[35]	中
MemCache线程	[36-39]	[36-39]	中


(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:508] Binding worker process threads. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 main_cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33] acl_cpus=[34] release_cpus=[35] thread_count=118
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker_DP tid=815572 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815583 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815584 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815585 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815586 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815587 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815588 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815589 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815590 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815591 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=AtraceMonitor tid=815598 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=WatchdogMonitor tid=815599 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=PlogFlush tid=815600 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815623 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815624 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815625 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815626 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815627 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815628 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815629 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815630 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815631 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815694 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815736 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=python tid=815737 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=adx_data_dump_t tid=815738 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=PlogReportRecv tid=815742 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=TraceClientRecv tid=815743 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=MONITOR_0 tid=815768 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=REPORT_RAS tid=815769 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=RT_RECYCLE tid=815770 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=pt_autograd_0 tid=815774 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=pt_autograd_1 tid=815775 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=pt_autograd_2 tid=815776 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=pt_autograd_3 tid=815777 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=pt_autograd_4 tid=815778 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=pt_autograd_5 tid=815779 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=pt_autograd_6 tid=815780 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=pt_autograd_7 tid=815781 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=815784 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=AOE_RTKB tid=815785 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=AOE_RTKB tid=815786 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=AOE_RTKB tid=815787 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=AOE_RTKB tid=815788 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=AOE_RTKB tid=815789 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=AOE_RTKB tid=815790 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=AOE_RTKB tid=815791 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=AOE_RTKB tid=815792 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=CaffeTaskThread tid=815793 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=CaffeTaskThread tid=815794 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=CaffeTaskThread tid=815795 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=CaffeTaskThread tid=815796 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=CaffeTaskThread tid=815797 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=hccl_watchdog_t tid=815798 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=hccl_watchdog_t tid=815799 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=815800 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816556 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816557 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=hccl_watchdog_t tid=816587 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816608 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816620 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816621 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=ZMQbg/Reaper tid=816651 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=ZMQbg/IO/0 tid=816654 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=hccl_watchdog_t tid=816665 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816689 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816721 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816722 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816734 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816765 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816766 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816778 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816797 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816798 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=hccl_watchdog_t tid=816799 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816836 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816868 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816871 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816892 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816921 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816925 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=hccl_watchdog_t tid=816948 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816962 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816995 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=816997 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=817009 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=817010 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=817011 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=817012 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=817013 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=817014 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=817015 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=817016 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker tid=817017 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker_DP tid=817490 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker_DP tid=819931 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=ZMQbg/Reaper tid=819932 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=ZMQbg/IO/0 tid=819933 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=ZMQbg/Reaper tid=819934 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=ZMQbg/IO/0 tid=819935 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=VLLM::Worker_DP tid=819937 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=Hccl_HeartBeat tid=821687 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=Hccl_ThrdManage tid=823712 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=Hccl_ThrdManage tid=823713 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=Hccl_ThrdManage tid=823714 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=Hccl_ThrdManage tid=823804 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=Hccl_ThrdManage tid=823805 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:522] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=Hccl_ThrdManage tid=823806 role=main cpus=[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:534] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=acl_thread tid=815771 role=acl cpus=[34]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:534] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=acl_thread tid=817888 role=acl cpus=[34]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:534] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=acl_thread tid=817889 role=acl cpus=[34]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:534] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=acl_thread tid=817891 role=acl cpus=[34]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:534] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=acl_thread tid=817894 role=acl cpus=[34]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:534] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=acl_thread tid=817890 role=acl cpus=[34]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:534] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=acl_thread tid=817892 role=acl cpus=[34]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:534] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=acl_thread tid=817893 role=acl cpus=[34]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:534] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=acl_thread tid=817887 role=acl cpus=[34]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:30 [cpu_binding.py:546] Binding worker thread. process_name=VLLM::Worker_DP0_TP1_EP1 pid=815572 thread_name=release_thread tid=815772 role=release cpus=[35]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:47 [cpu_binding.py:631] NPU1(PCI 0000:9f:00.0): sq_send_trigger_irq IRQ_ID=2039 -> CPU20, cq_update_irq IRQ_ID=2040 -> CPU21

(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:47 [memcache_backend.py:210] Temporarily expanded current thread CPUs from [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33] to [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 36, 37, 38, 39] while initializing MemCache store.
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:52 [memcache_backend.py:221] Restored current thread CPUs to [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33] after initializing MemCache store.
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=AccDelayClean tid=830229 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=AccWrk:0 tid=830230 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=AccWrk:1 tid=830231 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=config_store_hb tid=830232 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=ptracer_dump tid=830234 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=grp_listen_evt tid=830235 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=executor0 tid=830267 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=executor1 tid=830268 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=executor2 tid=830269 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=executor3 tid=830270 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=executor4 tid=830271 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=executor5 tid=830272 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=executor6 tid=830273 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=executor7 tid=830274 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=AccDelayClean tid=830744 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=AccWrk:0 tid=830745 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=AccWrk:1 tid=830746 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool0 tid=830747 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool1 tid=830748 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool2 tid=830749 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool3 tid=830750 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool4 tid=830751 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool5 tid=830752 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool6 tid=830753 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool7 tid=830754 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool8 tid=830755 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool9 tid=830756 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool10 tid=830757 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool11 tid=830758 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool12 tid=830759 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool13 tid=830760 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool14 tid=830761 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=net_pool15 tid=830762 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=client_pool0 tid=830763 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool0 tid=830764 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool1 tid=830765 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool2 tid=830766 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool3 tid=830767 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool4 tid=830768 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool5 tid=830769 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool6 tid=830770 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool7 tid=830771 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool8 tid=830772 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool9 tid=830773 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool10 tid=830774 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=read_pool11 tid=830775 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=write_pool0 tid=830776 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=write_pool1 tid=830777 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=write_pool2 tid=830778 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [memcache_backend.py:163] Bound MemCache thread name=write_pool3 tid=830779 to CPUs [36, 37, 38, 39]
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [pool_worker.py:241] Bound layerwise send thread 830834 to CPU36
(Worker_DP0_TP1_EP1 pid=815572) INFO 05-25 14:41:53 [pool_worker.py:241] Bound layerwise recv thread 830836 to CPU37
