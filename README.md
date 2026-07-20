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