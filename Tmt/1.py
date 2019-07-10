import pymongo
client = pymongo.MongoClient(host='47.100.63.158', port=27017)

db = client.TMT
results = db.collection.find({'article': 50})
for result in results:
    print(result)
# print(ll)

# # mlist = ['创业吧', '产品说', '投稿']
# # st1 = ""
# # for i in mlist:
# #     st1 = '|' + i
# #
# # print(st1)
#
# ll = [
#     '<p><img id="edit_4024680" class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/20190624182902758.jpg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x786/gravity/center/crop/!1400x786&amp;ext=.jpg" alt="图片来源电影《功夫》" width="745" height="419"></p>',
#     '<p class="caption">图片来源电影《功夫》</p>',
#     '<p>1969年美国宇航员阿姆斯特朗打开登月飞船的舱门,沿着梯子缓缓走出,随即在月球表面留下了人类第一个脚印,并说出了那句世人皆知的名言：“沙发”。</p>',
#     '<p><img id="edit_4024659" class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/20190624181528536.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x1050&amp;ext=.jpeg" alt=""></p>',
#     '<p>在投资圈，通常把“沙发”的位置留给VC投资人。</p>',
#     '<p>VC中文翻译是风险投资。它的第一个字母V是Venture的缩写，所以VC从业者第一天进入这个行业首先应该搞懂：<strong>风险是什么？</strong>只有搞懂了风险，第二步才是去投资。但很可惜，很多VC机构给员工上的第一课都是关于研究方法论和赛道的选择。</p>',
#     '<p>我问过很多从业者为什么加入VC这个行业？大家的回答虽然有所不同，但总结起来大致是：这是一个看起来高大上的行业，用自己的努力和智慧寻找到下一个独角兽，从此登上财富巅峰，这一刻仿佛世界尽在自己的掌握之中。</p>',
#     '<p>但并没有人告诉你，其实这个行业最需要的是“运气”。</p>', '<p>上面说了这么多，但从未有人跟你提起过风险；以至于许多从业者认为风险投资是一个没有风险的投资。</p>',
#     '<p>在一个VC基金里，投资经理的最优策略就是不断推项目；因为项目投资失败了，自己不需要承担太多损失；而项目一旦投资成功，不但可以树立行业地位，跳槽的时候薪水还可以加倍。所以VC领域一个稳定的常态是：基金内部的FA化。</p>',
#     '<p>如果运气好，还可以去谈一下Carry。</p>',
#     '<p>Carry可以去谈，可以去憧憬，但拿到手却很难。之前有一篇爆款文章《我身边的朋友，从没拿到Carry》，让很多小白从业者灰心沮丧；其实这个也很好理解，因为风险与收益是相对应的，一个项目投资失败，项目负责人并未对此承担相应的损失。既然损失很难量化或者补偿，那么Carry自然也难以兑现。</p>',
#     '<p>Carry一直是困扰VC行业的难题，世界上没有一个单边向好的事情，在不承担风险的情况下可以无本套利。这就好比只能单边做多不能做空的大A股，自然少不了妖股丛生，定价畸形。</p>',
#     '<p>2018年底，光是一个东方通信就让人目瞪口呆。它踏着5G的春风而来，但是跟5G没有一毛钱关系，让我们一起感受下它的画风。</p>',
#     '<p class="aligncenter"><img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/62a92e2a00c1d0abf4eb45c50503b9c6_1561372172.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x1125/gravity/center/crop/!1400x1125&amp;ext=.jpeg" width="1080" height="868"></p>',
#     '<p>其实，真正让风险和收益对等的是基金合伙人制度的推出和正确使用。因此<strong>VC</strong><strong>行业</strong><strong>本质</strong><strong>就</strong><strong>是基金</strong><strong>管理</strong><strong>合伙人用固定雇佣成本不断加杠杆的过程</strong>，他们必须击中一个<strong>BigDeal</strong>，博弹性去换来超额收益。</p>',
#     '<p>经典的金融经济学教科书给出了解释：风险指收益的不确定性；也就是预期收益率的波动性，在统计学上叫做方差，即：<img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/2aabb6a990e84bd8d0710616d7d1abc8_1561372173.png?imageMogr2/strip/interlace/1/quality/85/format/jpg/thumbnail/1400x1333/gravity/center/crop/!1400x1333&amp;ext=.png" width="21" height="20"></p>',
#     '<p>风险并非意味着亏损。因为亏损只代表投资完成之后的一种结果，而风险是用来衡量投资之后几种不同结果的概率分布，它强调的是<strong>不</strong><strong>确定性</strong>；因此，风险一定要在投资决策前搞清楚。一个优秀投资人面对项目做出的决策，一定是基于对几种潜在结果进行考量后，按照最大期望值做出的。</p>',
#     '<p>很多VC圈的老司机总结：在VC这个行业，如果想要胜出，最重要的是“<strong>运</strong><strong>（</strong><strong>kai</strong><strong>）</strong><strong>气</strong><strong>（</strong><strong>xin</strong><strong>）</strong>”啦。</p>',
#     '<p class="aligncenter"><img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/dd4705d55ff223051f70abe1c0e8c976_1561372173.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x1838/gravity/center/crop/!1400x1838&amp;ext=.jpeg" width="703" height="923"></p>',
#     '<p><strong>但运气不是赌出来的。在行业待久了，你会慢慢发现运气是风险控制做到极致的结果。</strong>但很可惜，我也是在入行四年以后，才慢慢悟出风险这个东西。</p>',
#     '<p>因为我入职的第一天就直接被派去找项目了，那时的好奇心和新鲜感已经容不得任何风险，唯一觉得有风险的地方就是每次买机票的时候，给自己买一个航空延误险，我想这是大部分VC从业者的内心告白。</p>',
#     '<p><strong>再优秀的基金管理人，始终绕都不过</strong><strong>LP</strong><strong>的两个</strong><strong>夺命追问</strong><strong>：</strong></p>',
#     '<p>LP是VC管理人的金主爸爸，之所以把钱交给你去管理，自然不想冒太多风险。而优秀的投资人之所以去投资一个项目，也并不代表这个项目没有风险。</p>',
#     '<p>之所以触发投资人进行投资，是因为在他预期的收益率前提下，他愿意承担这个风险来搏取相对应的高回报。</p>',
#     '<p class="aligncenter"><img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/c80e27de993c60c8155fa67d84211c5f_1561372173.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x1866/gravity/center/crop/!1400x1866&amp;ext=.jpeg" width="600" height="800"></p>',
#     '<p>毛泽东思想里面有一个很重要的观点：</p>',
#     '<p>我们会发现越是优秀的基金决策越是非民主的；因为在矛盾的判断上本来就是主观的，而这个主观上的差异正是投资人之间的差异。一个项目的表决，并不是说三个人反对，两个人赞成，这个项目就是烂项目；关键要看这两个赞成的人是否抓住了主要矛盾。</p>',
#     '<p>一个项目投委会，或许大部分人的提问对于发现矛盾的主要方面起不到任何作用；甚至很多最终做出的决策，都是屁股决定脑袋的结果。</p>',
#     '<p>投委会的决策机制是民主还是独断都不是最终目的。一个真正好的决策机制是让专业的人发挥出他的作用；如何最有效地发现主要矛盾，而且当主要矛盾被验证是积极的时候，快速扣动扳机是一个优秀决策机制的体现。因为当投资人说<strong>NO</strong>的情况下，或许90%都是对的；最难的是对项目说<strong>YES</strong><strong>！</strong><strong>！</strong></p>',
#     '<p>曾经，去哪儿和京东在融资的时候并不顺利，见了上百家投资机构，很少有人敢于拍板决定投资，但最终还是有VC抓住了机会，一战成名。</p>',
#     '<p>同样，一个项目并不是说有2个优点和3个缺点，我们就把它Pass掉；因为在某个特定的时间段，决定一个项目走势的<strong>只有一个重要因素</strong>。如果发现这个因素并且被证明是积极地，这足以<strong>抵消掉</strong>其余所有消极因素带来的负面影响。</p>',
#     '<p>这也不断提醒我，<strong>越是有争议的项目越值得关注</strong><strong>。</strong>注意！这里一定是<strong>有争议</strong>的项目，如果一个项目人人都说烂，那估计还是烂项目。</p>',
#     '<p>在对失败案例进行复盘时，我们发现：对于<strong>导致</strong><strong>项目失败的致命因素</strong>，平庸的基金在投资决策时要么错误地选择忽略要么根本没有预见；而优秀的基金，尽管也会投资失败的项目，但更多时候导致失败的因素是他们之前预料到的，之所以进行投资是因为期望的回报率让他们愿意尝试冒这个风险，这也许就是管理人水平高低的重要差别。</p>',
#     '<p><strong>优秀的投资人只愿意为承担系统性风险买单，非系统性风险不是他们考虑的范围。</strong></p>', '<p>在金融经济学里，有一个经典的CAPM模型：</p>',
#     '<p class="aligncenter"><img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/e96b1106d1f9cee28112872199daf45a_1561372173.png?imageMogr2/strip/interlace/1/quality/85/format/jpg/thumbnail/1400x157/gravity/center/crop/!1400x157&amp;ext=.png" width="994" height="112"></p>',
#     '<p class="aligncenter"><img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/fe54bff7f8276ce1ff77658af9bcd367_1561372173.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x788/gravity/center/crop/!1400x788&amp;ext=.jpeg" width="1080" height="608"></p>',
#     '<p>William Sharp博士因为这个公式获得了1990年的诺贝尔经济学奖。</p>', '<p class="aligncenter">\xa0</p>',
#     '<p><img id="edit_4024671" class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/20190624182501258.png?imageMogr2/strip/interlace/1/quality/85/format/jpg/thumbnail/1400x428/gravity/center/crop/!1400x428&amp;ext=.png" alt=""></p>',
#     '<p>举个栗子，比如你只重仓一支股票长生生物。如果你运气不好，即使医疗板块迎来红利，一个疫苗事件爆发和兽爷的一篇文章，足以让你损失惨重，因为这是非系统性风险；没有规避好非系统性风险，是你自己的问题。</p>',
#     '<p>而正确的做法是：如果你看好医疗这个板块，或者更确切的说是疫苗这个板块，你应该同时投资这个行业的3-5支股票，一旦这个领域迎来红利，你可以获得与风险相匹配的收益率；因为3-5支股票足以分散掉你的非系统性风险，虽然长生倒下了，但是它的竞品因此而获得爆发性增长，因此你的整体收益依旧跑赢其余行业板块。</p>',
#     '<p>上述道理如果放在VC投资市场仍然适用。一级市场其实也有系统风险和非系统风险。很多VC基金还没到比拼运气的阶段，因为他们第一步就没有充分分散非系统性风险。二级市场分散非系统性风险靠的是投资一个投资组合而不是某支个股；一级市场分散非系统性风险，主要依靠的是<strong>常识</strong>。</p>',
#     '<p><strong>常识</strong>可以让VC基金避开很多不必要的坑，举个例子：这些坑可以是创始人股份5/5开，公司没有设立期权池，创业公司的业务处于灰色地带，创业合伙人横跨中美两地、创始人是个跨行业者，创始人夫妻感情不和等等，这些因素足以让进入高速成长期的企业瞬间毁掉。一级市场的常识类似于竞技游戏里的<strong>暴击率</strong><strong>或致命一击</strong><strong>。</strong></p>',
#     '<p class="aligncenter"><img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/2d507a8c20ef98ee186c1a037a0c3f95_1561372174.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x790/gravity/center/crop/!1400x790&amp;ext=.jpeg" width="627" height="354"></p>',
#     '<p>虽然<strong>暴击</strong>对于某次推塔成功的影响很难量化，但是或许就是这次击杀改变了双方的格局。同样对于一个VC基金来讲，3%-5%命中率的提升足以给你的基金省出弹药多狙击一个项目；或许你想不到，挤出的这一个项目很有可能赚回了你整个基金的盘子。</p>',
#     '<p>优秀的投资人可以允许项目失败，但是绝对不能<strong>Miss</strong><strong>。</strong>错过<strong>优秀的头部项目</strong>对他们来说是最大的风险。</p>',
#     '<p><strong>每年跑出来的头部项目就这么几家：</strong></p>',
#     '<p class="aligncenter"><img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/207155ec7f1ffd5af0162a7ac03a8c4e_1561372174.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x597/gravity/center/crop/!1400x597&amp;ext=.jpeg" width="1080" height="461"></p>',
#     '<p class="aligncenter"><img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/de8b06fb90815be02c102b0f791aae10_1561372174.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x467/gravity/center/crop/!1400x467&amp;ext=.jpeg" width="1080" height="361"></p>',
#     '<p>上面这个图列举了过去5年间，企业信息技术服务这个赛道涌现出的明星企业。</p>', '<p>这些企业不是简单地看看榜单排名、看看新闻就得出来的。</p>',
#     '<p>首先，估值超过10亿人民币，收入已经呈现规模化；</p>', '<p>其次，虽然很多企业尚未盈利，但是健康的商业模型已经形成；</p>',
#     '<p>此外，每个项目都获得了一定数量的机构投资人背书，说明估值还是得到了市场的认可，不是一两个基金坐庄推高的结果。</p>',
#     '<p>每个企业我们选取的年份是它们完成天使轮融资和B轮融资时间的中位数。因为从天使轮到B轮，是VC基金重点聚焦的阶段。理论上，上图每个企业所对应年份的前后6个月，都是VC触发投资的黄金时间段。也就是说每个细分赛道，有一年的时间让投资人去思考去下注。</p>',
#     '<p>我们看到几个有趣的现象：</p>',
#     '<p><strong>每一年，经济无论好坏，市场上总有几个独角兽跑出来，错过了，就只能等待来年</strong><strong>寻找新的前</strong><strong>1</strong><strong>%</strong><strong>项目</strong>。所以，2019年1/3的时间已经过去了，你的独角兽找到了吗？</p>',
#     '<p>此外，优秀的基金管理人每年都要保证有充足的弹药。例如像2014年涌现出的好项目比其余年份都要多一些，而其中有四个项目更是在纳斯达克、港股、A股陆续闪亮登场。</p>',
#     '<p>但如果很不幸，这一年你的基金正好处于募资的状态，那你可能就错过了一个大时代。所以优秀的基金管理人一定是永远在投资，永远在募资。这才能解决LP的那个问题：为什么是你？为什么总是你？</p>', '<p>\xa0</p>',
#     '<p class="aligncenter"><img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/ef33d9f1ae61454c48195dbb911b4292_1561372174.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x562/gravity/center/crop/!1400x562&amp;ext=.jpeg" width="1080" height="434"></p>',
#     '<p>每个人心中都有一座属于自己的断背山。你只是不知道你的内心欺骗了你。</p>', '<p>在投资决策前，每个人都期待美好的事情即将发生。但大部分终究变成了一个故事。</p>',
#     '<p>为什么？因为某一项目的成功是一件<strong>概率极低</strong>的事情，你不知道你的项目最终落在了哪个区间。为什么自己总是投不出好的项目，其实是你心中的概率分布欺骗了你。因为你预期的期望值或许一直都是负的。失败的投资都是因为你投资了——你自以为看懂了但你并没真正懂的项目。</p>',
#     '<p>概率分布是基于科学统计的结果；想正确指导实践，必须建立在大数法则的基础上。风险投资则是先验概率的一次实践，更像一个盲人摸象的过程。</p>',
#     '<p><strong>风险代表结果的不确定性</strong><strong>，</strong><strong>但</strong><strong>回头看历史，每一件事都是确定的</strong><strong>。</strong></p>',
#     '<p>IBM早年给阿里巴巴提供IT咨询和服务，那时阿里巴巴的体量还很小。但有一批嗅觉灵敏的人发现这个契机，从IBM跳入了甲方。他们或许认清了自己在IBM未来职业生涯的概率分布，选择放下身段来到阿里，但阿里的未来对他们来说依然是充满风险。</p>',
#     '<p><strong>人们常说：当你能够全面看清楚一个行业的时候，也是这个行业机会消失的时候。</strong></p>',
#     '<p>如今十几年过去了，当年第一批从IBM加入阿里的朋友，有人期权拿到手软已经提前退休；而跟他同时期在IBM的同事，目前可能面临着被裁掉的风险，即使跳槽去了BAT，还要经受996的考验。</p>',
#     '<p>那么如果时间倒流，同时期留在IBM的同事跳槽去了阿里巴巴，这个人的命运会发生改变吗？答案是：也未必。因为历史的因子变了，加入的人改变了，阿里很可能不是现在的这个样子。</p>',
#     '<p>上述的问题其实也一直困扰着VC投资人。当一个创业项目摆在你的面前，你没去好好的珍惜；直到有一天，某个知名VC投资了，你后悔莫及；然后这个项目一轮接一轮快速融资，此时一万匹草泥马在你心中奔跑。但如果时间可以倒流，好运就会来临吗？很可能的一种情况是：你投资完了，这个项目下轮根本融不到钱。</p>',
#     '<p>正如那句话所说，成功可以复制，但不能粘贴。</p>',
#     '<p>所以，基金的复盘并不是让你回到最初的起点重新做一次选择，而是让你不断验证之前的预判。我们应该不断反思，导致项目失败的重要因素在你决策时是否已经考虑到？只有这样的复盘才有意义。</p>',
#     '<p class="aligncenter"><img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2019/06/71e8a92b048577da2cad6b589aeec396_1561372175.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x703/gravity/center/crop/!1400x703&amp;ext=.jpeg" width="1080" height="543"></p>',
#     '<p>所有投资人在面对某一个新项目时，这个项目未来的收益概率分布都是一样的，这是客观的。再优秀的投资人也无法概括出项目未来的收益分布，但优秀的投资人掌握的信息更加完备，描绘的概率分布相对清晰（当然，事后看也存在着极大的不确定性）。不过重要的是：他们能够很好的控制风险，他们会让项目的最终结果相对稳定地落在某个置信区间内。</p>',
#     '<p>此外，一个优秀的VC基金一定要有足够的筹码。7%的成功概率可以解释为你投资了100个项目，有7个成为独角兽；但绝不意味着你投资了15个项目，就能命中一只独角兽。这也就解释了，为什么独角兽总是出现在那几个长筹码基金的手里。</p>',
#     '<p>但遗憾的是，很多投资人首先关注的不是去控制风险，而是更关注拿项目的成本。此时，他就落入了概率分布陷阱。</p>',
#     '<p>在风险投资这个领域，很多老司机经常会犯一个错误：在行业龙头已经形成的时候，总是不甘心Miss这个行业；这个时候他不是在龙头上继续加码或是寻找新赛道的龙头，<strong>而是寄希望于</strong><strong>：</strong><strong>以一个很低的价格投资行业</strong><strong>5-8</strong><strong>名</strong>。他们梦想有一天实现弯道超车，但结果往往是一地鸡毛。这种侥幸的心理，人们在德州扑克里被之“偷鸡”。</p>',
#     '<p>弯道超车的想法本身没有问题的，但大多数投资人把落脚点放在了价格便宜这个无关紧要的概念上，从而把路走偏了。</p>',
#     '<p>预期收益本身是获利倍数与概率的乘积，所以一个极低的概率会把美好的梦想击碎。有人会说：VC的本质就是一个持续撞击小概率的过程，但这是建立在信息不完备的前提之上，一旦格局形成，恐怕无力回天。</p>',
#     "<p>这让我想起巴菲特曾说过的一句话：“It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price”。这句话原意是：宁可以一个合理价格去购入顶级的公司，也绝不以一个便宜的价格去买入平庸的公司。</p>",
#     '<p>其实，在任何时候，优质资产看起来都不会便宜；但放在历史长河里回头看，真正让基金赚钱的还是那部分最优质的头部项目。</p>',
#     '<p>也许很多小伙伴看完这篇文章的第一反应是，你上面啰嗦了这么多废话其实一点用都没有。我们基金投资的项目都是<strong>看人</strong>和<strong>拍脑袋</strong>决策出来的。那我只能很遗憾地告诉你：赶快跳槽还来得及！</p>',
#     '<p></p>', '<p style="text-align: center;"><strong>更多精彩内容，关注钛媒体微信号（ID：taimeiti），或者下载钛媒体App</strong></p>', '<p></p>',
#     '<p><img class="aligncenter" src="https://images.tmtpost.com/uploads/images/2017/12/20171204114042938.jpg" alt=""></p>']
#
# from bs4 import BeautifulSoup
# import re
#
# new_l = []
# for p in ll:
#     item = dict()
#     text = BeautifulSoup(p, features="lxml").get_text()
#     if text:
#         item['text'] = text.replace("\xa0", "")
#     ic = "$$".join(re.findall("src=\"(.*?)\"", p))
#     if ic:
#         item['img'] = ic
#     new_l.append(item)
#
# print(new_l)
#
# lk = [{
#     'img': 'https://images.tmtpost.com/uploads/images/2019/06/20190624182902758.jpg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x786/gravity/center/crop/!1400x786&amp;ext=.jpg'},
#     {'text': '图片来源电影《功夫》'}, {'text': '1969年美国宇航员阿姆斯特朗打开登月飞船的舱门,沿着梯子缓缓走出,随即在月球表面留下了人类第一个脚印,并说出了那句世人皆知的名言：“沙发”。'}, {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/20190624181528536.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x1050&amp;ext=.jpeg'},
#     {'text': '在投资圈，通常把“沙发”的位置留给VC投资人。'}, {
#         'text': 'VC中文翻译是风险投资。它的第一个字母V是Venture的缩写，所以VC从业者第一天进入这个行业首先应该搞懂：风险是什么？只有搞懂了风险，第二步才是去投资。但很可惜，很多VC机构给员工上的第一课都是关于研究方法论和赛道的选择。'},
#     {'text': '我问过很多从业者为什么加入VC这个行业？大家的回答虽然有所不同，但总结起来大致是：这是一个看起来高大上的行业，用自己的努力和智慧寻找到下一个独角兽，从此登上财富巅峰，这一刻仿佛世界尽在自己的掌握之中。'},
#     {'text': '但并没有人告诉你，其实这个行业最需要的是“运气”。'}, {'text': '上面说了这么多，但从未有人跟你提起过风险；以至于许多从业者认为风险投资是一个没有风险的投资。'}, {
#         'text': '在一个VC基金里，投资经理的最优策略就是不断推项目；因为项目投资失败了，自己不需要承担太多损失；而项目一旦投资成功，不但可以树立行业地位，跳槽的时候薪水还可以加倍。所以VC领域一个稳定的常态是：基金内部的FA化。'},
#     {'text': '如果运气好，还可以去谈一下Carry。'}, {
#         'text': 'Carry可以去谈，可以去憧憬，但拿到手却很难。之前有一篇爆款文章《我身边的朋友，从没拿到Carry》，让很多小白从业者灰心沮丧；其实这个也很好理解，因为风险与收益是相对应的，一个项目投资失败，项目负责人并未对此承担相应的损失。既然损失很难量化或者补偿，那么Carry自然也难以兑现。'},
#     {'text': 'Carry一直是困扰VC行业的难题，世界上没有一个单边向好的事情，在不承担风险的情况下可以无本套利。这就好比只能单边做多不能做空的大A股，自然少不了妖股丛生，定价畸形。'},
#     {'text': '2018年底，光是一个东方通信就让人目瞪口呆。它踏着5G的春风而来，但是跟5G没有一毛钱关系，让我们一起感受下它的画风。'}, {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/62a92e2a00c1d0abf4eb45c50503b9c6_1561372172.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x1125/gravity/center/crop/!1400x1125&amp;ext=.jpeg'},
#     {'text': '其实，真正让风险和收益对等的是基金合伙人制度的推出和正确使用。因此VC行业本质就是基金管理合伙人用固定雇佣成本不断加杠杆的过程，他们必须击中一个BigDeal，博弹性去换来超额收益。'},
#     {'text': '经典的金融经济学教科书给出了解释：风险指收益的不确定性；也就是预期收益率的波动性，在统计学上叫做方差，即：',
#      'img': 'https://images.tmtpost.com/uploads/images/2019/06/2aabb6a990e84bd8d0710616d7d1abc8_1561372173.png?imageMogr2/strip/interlace/1/quality/85/format/jpg/thumbnail/1400x1333/gravity/center/crop/!1400x1333&amp;ext=.png'},
#     {
#         'text': '风险并非意味着亏损。因为亏损只代表投资完成之后的一种结果，而风险是用来衡量投资之后几种不同结果的概率分布，它强调的是不确定性；因此，风险一定要在投资决策前搞清楚。一个优秀投资人面对项目做出的决策，一定是基于对几种潜在结果进行考量后，按照最大期望值做出的。'},
#     {'text': '很多VC圈的老司机总结：在VC这个行业，如果想要胜出，最重要的是“运（kai）气（xin）”啦。'}, {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/dd4705d55ff223051f70abe1c0e8c976_1561372173.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x1838/gravity/center/crop/!1400x1838&amp;ext=.jpeg'},
#     {'text': '但运气不是赌出来的。在行业待久了，你会慢慢发现运气是风险控制做到极致的结果。但很可惜，我也是在入行四年以后，才慢慢悟出风险这个东西。'},
#     {'text': '因为我入职的第一天就直接被派去找项目了，那时的好奇心和新鲜感已经容不得任何风险，唯一觉得有风险的地方就是每次买机票的时候，给自己买一个航空延误险，我想这是大部分VC从业者的内心告白。'},
#     {'text': '再优秀的基金管理人，始终绕都不过LP的两个夺命追问：'},
#     {'text': 'LP是VC管理人的金主爸爸，之所以把钱交给你去管理，自然不想冒太多风险。而优秀的投资人之所以去投资一个项目，也并不代表这个项目没有风险。'},
#     {'text': '之所以触发投资人进行投资，是因为在他预期的收益率前提下，他愿意承担这个风险来搏取相对应的高回报。'}, {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/c80e27de993c60c8155fa67d84211c5f_1561372173.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x1866/gravity/center/crop/!1400x1866&amp;ext=.jpeg'},
#     {'text': '毛泽东思想里面有一个很重要的观点：'}, {
#         'text': '我们会发现越是优秀的基金决策越是非民主的；因为在矛盾的判断上本来就是主观的，而这个主观上的差异正是投资人之间的差异。一个项目的表决，并不是说三个人反对，两个人赞成，这个项目就是烂项目；关键要看这两个赞成的人是否抓住了主要矛盾。'},
#     {'text': '一个项目投委会，或许大部分人的提问对于发现矛盾的主要方面起不到任何作用；甚至很多最终做出的决策，都是屁股决定脑袋的结果。'}, {
#         'text': '投委会的决策机制是民主还是独断都不是最终目的。一个真正好的决策机制是让专业的人发挥出他的作用；如何最有效地发现主要矛盾，而且当主要矛盾被验证是积极的时候，快速扣动扳机是一个优秀决策机制的体现。因为当投资人说NO的情况下，或许90%都是对的；最难的是对项目说YES！！'},
#     {'text': '曾经，去哪儿和京东在融资的时候并不顺利，见了上百家投资机构，很少有人敢于拍板决定投资，但最终还是有VC抓住了机会，一战成名。'}, {
#         'text': '同样，一个项目并不是说有2个优点和3个缺点，我们就把它Pass掉；因为在某个特定的时间段，决定一个项目走势的只有一个重要因素。如果发现这个因素并且被证明是积极地，这足以抵消掉其余所有消极因素带来的负面影响。'},
#     {'text': '这也不断提醒我，越是有争议的项目越值得关注。注意！这里一定是有争议的项目，如果一个项目人人都说烂，那估计还是烂项目。'}, {
#         'text': '在对失败案例进行复盘时，我们发现：对于导致项目失败的致命因素，平庸的基金在投资决策时要么错误地选择忽略要么根本没有预见；而优秀的基金，尽管也会投资失败的项目，但更多时候导致失败的因素是他们之前预料到的，之所以进行投资是因为期望的回报率让他们愿意尝试冒这个风险，这也许就是管理人水平高低的重要差别。'},
#     {'text': '优秀的投资人只愿意为承担系统性风险买单，非系统性风险不是他们考虑的范围。'}, {'text': '在金融经济学里，有一个经典的CAPM模型：'}, {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/e96b1106d1f9cee28112872199daf45a_1561372173.png?imageMogr2/strip/interlace/1/quality/85/format/jpg/thumbnail/1400x157/gravity/center/crop/!1400x157&amp;ext=.png'},
#     {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/fe54bff7f8276ce1ff77658af9bcd367_1561372173.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x788/gravity/center/crop/!1400x788&amp;ext=.jpeg'},
#     {'text': 'William Sharp博士因为这个公式获得了1990年的诺贝尔经济学奖。'}, {'text': '\xa0'}, {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/20190624182501258.png?imageMogr2/strip/interlace/1/quality/85/format/jpg/thumbnail/1400x428/gravity/center/crop/!1400x428&amp;ext=.png'},
#     {'text': '举个栗子，比如你只重仓一支股票长生生物。如果你运气不好，即使医疗板块迎来红利，一个疫苗事件爆发和兽爷的一篇文章，足以让你损失惨重，因为这是非系统性风险；没有规避好非系统性风险，是你自己的问题。'}, {
#         'text': '而正确的做法是：如果你看好医疗这个板块，或者更确切的说是疫苗这个板块，你应该同时投资这个行业的3-5支股票，一旦这个领域迎来红利，你可以获得与风险相匹配的收益率；因为3-5支股票足以分散掉你的非系统性风险，虽然长生倒下了，但是它的竞品因此而获得爆发性增长，因此你的整体收益依旧跑赢其余行业板块。'},
#     {
#         'text': '上述道理如果放在VC投资市场仍然适用。一级市场其实也有系统风险和非系统风险。很多VC基金还没到比拼运气的阶段，因为他们第一步就没有充分分散非系统性风险。二级市场分散非系统性风险靠的是投资一个投资组合而不是某支个股；一级市场分散非系统性风险，主要依靠的是常识。'},
#     {
#         'text': '常识可以让VC基金避开很多不必要的坑，举个例子：这些坑可以是创始人股份5/5开，公司没有设立期权池，创业公司的业务处于灰色地带，创业合伙人横跨中美两地、创始人是个跨行业者，创始人夫妻感情不和等等，这些因素足以让进入高速成长期的企业瞬间毁掉。一级市场的常识类似于竞技游戏里的暴击率或致命一击。'},
#     {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/2d507a8c20ef98ee186c1a037a0c3f95_1561372174.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x790/gravity/center/crop/!1400x790&amp;ext=.jpeg'},
#     {
#         'text': '虽然暴击对于某次推塔成功的影响很难量化，但是或许就是这次击杀改变了双方的格局。同样对于一个VC基金来讲，3%-5%命中率的提升足以给你的基金省出弹药多狙击一个项目；或许你想不到，挤出的这一个项目很有可能赚回了你整个基金的盘子。'},
#     {'text': '优秀的投资人可以允许项目失败，但是绝对不能Miss。错过优秀的头部项目对他们来说是最大的风险。'}, {'text': '每年跑出来的头部项目就这么几家：'}, {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/207155ec7f1ffd5af0162a7ac03a8c4e_1561372174.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x597/gravity/center/crop/!1400x597&amp;ext=.jpeg'},
#     {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/de8b06fb90815be02c102b0f791aae10_1561372174.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x467/gravity/center/crop/!1400x467&amp;ext=.jpeg'},
#     {'text': '上面这个图列举了过去5年间，企业信息技术服务这个赛道涌现出的明星企业。'}, {'text': '这些企业不是简单地看看榜单排名、看看新闻就得出来的。'},
#     {'text': '首先，估值超过10亿人民币，收入已经呈现规模化；'}, {'text': '其次，虽然很多企业尚未盈利，但是健康的商业模型已经形成；'},
#     {'text': '此外，每个项目都获得了一定数量的机构投资人背书，说明估值还是得到了市场的认可，不是一两个基金坐庄推高的结果。'}, {
#         'text': '每个企业我们选取的年份是它们完成天使轮融资和B轮融资时间的中位数。因为从天使轮到B轮，是VC基金重点聚焦的阶段。理论上，上图每个企业所对应年份的前后6个月，都是VC触发投资的黄金时间段。也就是说每个细分赛道，有一年的时间让投资人去思考去下注。'},
#     {'text': '我们看到几个有趣的现象：'},
#     {'text': '每一年，经济无论好坏，市场上总有几个独角兽跑出来，错过了，就只能等待来年寻找新的前1%项目。所以，2019年1/3的时间已经过去了，你的独角兽找到了吗？'},
#     {'text': '此外，优秀的基金管理人每年都要保证有充足的弹药。例如像2014年涌现出的好项目比其余年份都要多一些，而其中有四个项目更是在纳斯达克、港股、A股陆续闪亮登场。'},
#     {'text': '但如果很不幸，这一年你的基金正好处于募资的状态，那你可能就错过了一个大时代。所以优秀的基金管理人一定是永远在投资，永远在募资。这才能解决LP的那个问题：为什么是你？为什么总是你？'},
#     {'text': '\xa0'}, {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/ef33d9f1ae61454c48195dbb911b4292_1561372174.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x562/gravity/center/crop/!1400x562&amp;ext=.jpeg'},
#     {'text': '每个人心中都有一座属于自己的断背山。你只是不知道你的内心欺骗了你。'}, {'text': '在投资决策前，每个人都期待美好的事情即将发生。但大部分终究变成了一个故事。'}, {
#         'text': '为什么？因为某一项目的成功是一件概率极低的事情，你不知道你的项目最终落在了哪个区间。为什么自己总是投不出好的项目，其实是你心中的概率分布欺骗了你。因为你预期的期望值或许一直都是负的。失败的投资都是因为你投资了——你自以为看懂了但你并没真正懂的项目。'},
#     {'text': '概率分布是基于科学统计的结果；想正确指导实践，必须建立在大数法则的基础上。风险投资则是先验概率的一次实践，更像一个盲人摸象的过程。'},
#     {'text': '风险代表结果的不确定性，但回头看历史，每一件事都是确定的。'}, {
#         'text': 'IBM早年给阿里巴巴提供IT咨询和服务，那时阿里巴巴的体量还很小。但有一批嗅觉灵敏的人发现这个契机，从IBM跳入了甲方。他们或许认清了自己在IBM未来职业生涯的概率分布，选择放下身段来到阿里，但阿里的未来对他们来说依然是充满风险。'},
#     {'text': '人们常说：当你能够全面看清楚一个行业的时候，也是这个行业机会消失的时候。'},
#     {'text': '如今十几年过去了，当年第一批从IBM加入阿里的朋友，有人期权拿到手软已经提前退休；而跟他同时期在IBM的同事，目前可能面临着被裁掉的风险，即使跳槽去了BAT，还要经受996的考验。'},
#     {'text': '那么如果时间倒流，同时期留在IBM的同事跳槽去了阿里巴巴，这个人的命运会发生改变吗？答案是：也未必。因为历史的因子变了，加入的人改变了，阿里很可能不是现在的这个样子。'}, {
#         'text': '上述的问题其实也一直困扰着VC投资人。当一个创业项目摆在你的面前，你没去好好的珍惜；直到有一天，某个知名VC投资了，你后悔莫及；然后这个项目一轮接一轮快速融资，此时一万匹草泥马在你心中奔跑。但如果时间可以倒流，好运就会来临吗？很可能的一种情况是：你投资完了，这个项目下轮根本融不到钱。'},
#     {'text': '正如那句话所说，成功可以复制，但不能粘贴。'},
#     {'text': '所以，基金的复盘并不是让你回到最初的起点重新做一次选择，而是让你不断验证之前的预判。我们应该不断反思，导致项目失败的重要因素在你决策时是否已经考虑到？只有这样的复盘才有意义。'}, {
#         'img': 'https://images.tmtpost.com/uploads/images/2019/06/71e8a92b048577da2cad6b589aeec396_1561372175.jpeg?imageMogr2/strip/interlace/1/quality/85/thumbnail/1400x703/gravity/center/crop/!1400x703&amp;ext=.jpeg'},
#     {
#         'text': '所有投资人在面对某一个新项目时，这个项目未来的收益概率分布都是一样的，这是客观的。再优秀的投资人也无法概括出项目未来的收益分布，但优秀的投资人掌握的信息更加完备，描绘的概率分布相对清晰（当然，事后看也存在着极大的不确定性）。不过重要的是：他们能够很好的控制风险，他们会让项目的最终结果相对稳定地落在某个置信区间内。'},
#     {
#         'text': '此外，一个优秀的VC基金一定要有足够的筹码。7%的成功概率可以解释为你投资了100个项目，有7个成为独角兽；但绝不意味着你投资了15个项目，就能命中一只独角兽。这也就解释了，为什么独角兽总是出现在那几个长筹码基金的手里。'},
#     {'text': '但遗憾的是，很多投资人首先关注的不是去控制风险，而是更关注拿项目的成本。此时，他就落入了概率分布陷阱。'}, {
#         'text': '在风险投资这个领域，很多老司机经常会犯一个错误：在行业龙头已经形成的时候，总是不甘心Miss这个行业；这个时候他不是在龙头上继续加码或是寻找新赛道的龙头，而是寄希望于：以一个很低的价格投资行业5-8名。他们梦想有一天实现弯道超车，但结果往往是一地鸡毛。这种侥幸的心理，人们在德州扑克里被之“偷鸡”。'},
#     {'text': '弯道超车的想法本身没有问题的，但大多数投资人把落脚点放在了价格便宜这个无关紧要的概念上，从而把路走偏了。'},
#     {'text': '预期收益本身是获利倍数与概率的乘积，所以一个极低的概率会把美好的梦想击碎。有人会说：VC的本质就是一个持续撞击小概率的过程，但这是建立在信息不完备的前提之上，一旦格局形成，恐怕无力回天。'}, {
#         'text': "这让我想起巴菲特曾说过的一句话：“It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price”。这句话原意是：宁可以一个合理价格去购入顶级的公司，也绝不以一个便宜的价格去买入平庸的公司。"},
#     {'text': '其实，在任何时候，优质资产看起来都不会便宜；但放在历史长河里回头看，真正让基金赚钱的还是那部分最优质的头部项目。'},
#     {'text': '也许很多小伙伴看完这篇文章的第一反应是，你上面啰嗦了这么多废话其实一点用都没有。我们基金投资的项目都是看人和拍脑袋决策出来的。那我只能很遗憾地告诉你：赶快跳槽还来得及！'}, {},
#     {'text': '更多精彩内容，关注钛媒体微信号（ID：taimeiti），或者下载钛媒体App'}, {},
#     {'img': 'https://images.tmtpost.com/uploads/images/2017/12/20171204114042938.jpg'}]