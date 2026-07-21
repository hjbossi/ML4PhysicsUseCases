# ML4PhysicsUseCases

## Sources for Figure 1
### Netflix
    - 1GB/hour https://help.netflix.com/en/node/87
    - 523 million hours / day https://www.statspanda.com/live-counters/netflix-hours-watched-globally
    - Dimensional analyis gives 190,895 PB / year

### Global Emails 
    - 392.5 billion emails sent per day: https://www.emailtooltester.com/en/blog/how-many-emails-are-sent-per-day/
    - 75 KB/email https://mailmeteor.com/tools/email-size
    - Dimensional analysis gives 10,744 PB/year 

### Spam Emails
    - Based on the estimate that 45.6% of emails are spam https://debounce.com/blog/email-spam-statistics/
    - So then that is 178.98 billion emails per day 
    - 75 KB/email https://mailmeteor.com/tools/email-size
    - Dimensional analysis gives 4,900 PB/year 

### YouTube Uploads
    - 720,000 hours of YouTube Uploads/day https://www.statspanda.com/live-counters/hours-of-video-uploaded-to-youtube
    - Assuming 720p (HD) video (middle tier), 1.95 GB/hour https://www.firsty.app/help/general/how-much-data-does-youtube-use
    - Dimensional Analysis gives 512.46 PB/ year

## LHC Grid Data Streaming
    - 10 Pb/day in Run 3: epj-conferences.org/articles/epjconf/pdf/2025/22/epjconf_chep2025_01327.pdf
    - Dimensional analysis gives 3,650 PB/year

### AWS Storage
    - 350 T objects total (2026) https://sqmagazine.co.uk/aws-statistics/
    - Using 1 MB average https://www.reddit.com/r/aws/comments/1hgd0o3/average_s3_object_size/
    - Dimensional analysis gives 350k PB total storage

### Google Web Index
    - 400 billion web pages https://zyppy.com/seo/google-index-size/ (see also https://thecapitolforum.com/google_antitrust_trial_2023/)
    - average size of a page is 2.5 MB (https://www.debugbear.com/blog/page-weight-website-speed)
    - 1,000 PB

### Dropbox
     - 700 million users, 18 million paid users https://sqmagazine.co.uk/dropbox-statistics/
     - 682 million users on free plan, which is 2 GB, so 1,364 PB just from free users
     - 18 million users on paid plan, use lowest tier of 2 TB to account for the fact that most users don't use the full thing, from this, 36,000 PB 
     - From this you get 37,364 PB 

### LHC Grid Total Stored
    - 1500 PB from https://home.cern/science/computing/grid/ 

### Vera Rubin Observatory 
    - 10 TB/day https://rubinobservatory.org/explore/how-rubin-works/technology/data
    - Dimensional analysis gives 3650 TB / year = 3.65 PB / year

### SKA observatory
    - 700 PB/year https://www.skao.int/en/explore/big-data

### LHC Run 3 data 
    - 200 PB/year https://chtc.cs.wisc.edu/wlcg-collaboration.html

### LHC Run 3 MC 
    - MC generated seems to be 3x the data recorded: https://cds.cern.ch/record/2716461/files/10.1007_s41781-021-00055-1.pdf

### HL-LHC Data
    - Take values from figure 5 from https://cds.cern.ch/record/2815292/files/NOTE2022_008.pdf
    - 300 PB on disk per year
    - 800 PB tape 
    - 1100 PB/year total 

### HL-LHC MC
    - Use same factor 3 number from above, 3300 PB/year

### HL-LHC (hypothetical)
    - This is designed to be what you get if you don't trigger
    - CMS detector has ~100M readout channels
    - Each channel produces ~10 bits per bunch crossing at 40 MHz collision rate
    - 100×10⁶ channels × 10 bits × 40×10⁶ Hz = 4×10¹⁶ bits/s = ~5 PB/s
    - 5 PB/s × 3.15×10⁷ s/yr ≈ 1.6×10⁸ PB/yr per experiment → ~10⁸ PB/yr order of magnitude
    - This is why the trigger system exists — it reduces this by a factor of ~10⁶


## Sources for Figure 2

### LHC L1T 
    - LHC L1T — latency 4×10⁻⁶ s, rate 2×10¹² B/s, 500 PB/yr
    - Latency: CMS Run 3 L1T hardware latency is publicly documented at 4 μs https://iopscience.iop.org/article/10.1088/1748-0221/15/10/P10017
    - Rate: The L1T FPGA fabric must inspect trigger primitives from all sub-detectors at 40 MHz. Total primitive bandwidth across all subsystems is O(1–10 TB/s); I used 2 TB/s = 2×10¹² B/s as a central estimate based on https://indico.cern.ch/event/1517284/contributions/6385565/attachments/3080674/5452992/NGT_CMS_SecondAllHands.pdf 
    - Annual volume:  ~200 PB/yr — consistent with numbers from previous figure

### LHC HLT 
    - 260 ms as the latency https://indico.cern.ch/event/1199314/contributions/5240253/attachments/2619778/4529140/DSLemos_Trigger_DIS23_v4.pdf
    - 2 TB/s https://cms.cern/news/cms-completes-new-daq-server-room-preparation-hi-lumi 

### DUNE 
    - Latency: DUNE online trigger must correlate with the Fermilab beam spill window (~10 us) https://indico.snolab.ca/event/21/contributions/578/attachments/441/917/DUNE_ingratta_NNN25.pdf
    - Rate: Far detector module 1 has ~800 000 readout channels at 2 MHz, 12-bit ADC → 2.4 TB/s raw.
    -  ~30 PB/yr for Phase I https://inspirehep.net/files/0e41ade808aa571c69628e3ac00cffa7  

###  Google Cloud
    - Latency: Tested response time https://www.gcping.com/ and max latecy was 750 ms, so 0.75 s
    - Rate: Publisher throughput per region (mediums) 800 MB/s https://docs.cloud.google.com/pubsub/quotas
    - Annual volume: 100 zettabytes total https://www.pump.co/blog/cloud-computing-growth-statistics/ and then google cloud has 14% of this so that is roughly 1.4 e22 bytes

###  SKA Observatory 
    - 700 PB/year https://www.skao.int/en/explore/big-data (previous fig)
    - Rate: 8 TB/s https://www.skao.int/en/explore/big-data
    - Latency: 10 s https://www.skao.int/sites/default/files/documents/SCIOPS_TIMELINE_MID.pdf 

### Vera Rubin Observatory 
    - 3.65 PB / year based on the above plot
    - Take 10 TB/hour and do dimensional analysis to get: 2.7e9 B/s
    - Latency of 60 sec https://rubinobservatory.org/for-scientists/rubin-101/key-numbers

### LIGO
    - Rate: 80 MB/s https://www.linkedin.com/posts/gabriele-vajente_how-much-data-does-ligo-produce-the-main-activity-7467942489581228035-AMYD/
    - Latency: 29.5s https://www.pnas.org/doi/10.1073/pnas.2316474121
    - Total volume 0.8 B/year: https://www.eoportal.org/other-space-activities/ligo#precision-characterization 

### Ice Cube
    - Rate: 100 Gb/s https://internet2.edu/can-we-use-all-the-bandwidth/
    - Total volume 130 TB or 0.13 Pb: https://internet2.edu/can-we-use-all-the-bandwidth/
    - Latency: 30 s https://iopscience.iop.org/article/10.3847/1538-4357/aca5fc

### Netflix
    - Convert 523 million hours / day https://www.statspanda.com/live-counters/netflix-hours-watched-globally to bytes per second, 6.05324074 × 10^12 b/s
    - 190,895 PB / year for the previous plot to
    - 200s https://www.mux.com/articles/adaptive-bitrate-streaming-how-it-works-and-how-to-get-it-right