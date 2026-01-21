// All templates from .claude/templates/ organized by platform

export interface Template {
  id: string
  name: string
  category: string
  platform: 'linkedin' | 'twitter' | 'instagram' | 'email'
  type: string
  description: string
  path: string
}

export const templates: Template[] = [
  // LinkedIn Templates
  // Connection Requests
  { id: 'li-cr-cold', name: 'Cold Outreach', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Initial cold connection request', path: 'linkedin/connection-requests/cold_outreach.md' },
  { id: 'li-cr-mutual', name: 'Mutual Connection', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Leverage mutual connections', path: 'linkedin/connection-requests/mutual_connection.md' },
  { id: 'li-cr-industry', name: 'Same Industry', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Industry peer connection', path: 'linkedin/connection-requests/same_industry.md' },
  { id: 'li-cr-recruiter', name: 'Recruiter', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Recruiter outreach', path: 'linkedin/connection-requests/recruiter.md' },
  { id: 'li-cr-investor', name: 'Investor Outreach', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Connect with investors', path: 'linkedin/connection-requests/investor_outreach.md' },
  { id: 'li-cr-event', name: 'Event Attendee', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Post-event follow-up', path: 'linkedin/connection-requests/event_attendee.md' },
  { id: 'li-cr-founder', name: 'Startup Founder', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Founder to founder', path: 'linkedin/connection-requests/startup_founder.md' },
  { id: 'li-cr-thought', name: 'Thought Leader', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Connect with thought leaders', path: 'linkedin/connection-requests/thought_leader.md' },
  { id: 'li-cr-speaker', name: 'Speaker Invitation', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Invite as speaker', path: 'linkedin/connection-requests/speaker_invitation.md' },
  { id: 'li-cr-content', name: 'Content Collaboration', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Content partnership', path: 'linkedin/connection-requests/content_collaboration.md' },
  { id: 'li-cr-alumni', name: 'Alumni Connect', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Alumni network', path: 'linkedin/connection-requests/alumni_connect.md' },
  { id: 'li-cr-client', name: 'Potential Client', category: 'Connection Requests', platform: 'linkedin', type: 'connection', description: 'Sales prospect', path: 'linkedin/connection-requests/potential_client.md' },

  // LinkedIn Messages
  { id: 'li-msg-intro', name: 'Intro After Connect', category: 'Messages', platform: 'linkedin', type: 'message', description: 'First message after connecting', path: 'linkedin/messages/intro_after_connect.md' },
  { id: 'li-msg-follow', name: 'Follow Up No Response', category: 'Messages', platform: 'linkedin', type: 'message', description: 'Follow up when no reply', path: 'linkedin/messages/follow_up_no_response.md' },
  { id: 'li-msg-meeting', name: 'Meeting Request', category: 'Messages', platform: 'linkedin', type: 'message', description: 'Request a meeting', path: 'linkedin/messages/meeting_request.md' },
  { id: 'li-msg-collab', name: 'Collaboration Proposal', category: 'Messages', platform: 'linkedin', type: 'message', description: 'Propose collaboration', path: 'linkedin/messages/collaboration_proposal.md' },
  { id: 'li-msg-value', name: 'Value Offer', category: 'Messages', platform: 'linkedin', type: 'message', description: 'Offer value first', path: 'linkedin/messages/value_offer.md' },
  { id: 'li-msg-thanks', name: 'Thank You', category: 'Messages', platform: 'linkedin', type: 'message', description: 'Thank you message', path: 'linkedin/messages/thank_you.md' },
  { id: 'li-msg-partner', name: 'Partnership Proposal', category: 'Messages', platform: 'linkedin', type: 'message', description: 'Business partnership', path: 'linkedin/messages/partnership_proposal.md' },
  { id: 'li-msg-sales', name: 'Sales Intro', category: 'Messages', platform: 'linkedin', type: 'message', description: 'Sales introduction', path: 'linkedin/messages/sales_intro.md' },
  { id: 'li-msg-referral', name: 'Referral Request', category: 'Messages', platform: 'linkedin', type: 'message', description: 'Ask for referral', path: 'linkedin/messages/referral_request.md' },
  { id: 'li-msg-expert', name: 'Expertise Request', category: 'Messages', platform: 'linkedin', type: 'message', description: 'Ask for expertise', path: 'linkedin/messages/expertise_request.md' },
  { id: 'li-msg-podcast', name: 'Podcast Invitation', category: 'Messages', platform: 'linkedin', type: 'message', description: 'Invite to podcast', path: 'linkedin/messages/podcast_invitation.md' },

  // LinkedIn InMails
  { id: 'li-im-cold', name: 'Cold InMail', category: 'InMails', platform: 'linkedin', type: 'inmail', description: 'Cold InMail outreach', path: 'linkedin/inmails/cold_inmail.md' },
  { id: 'li-im-exec', name: 'Executive Outreach', category: 'InMails', platform: 'linkedin', type: 'inmail', description: 'Reach executives', path: 'linkedin/inmails/executive_outreach.md' },
  { id: 'li-im-job', name: 'Job Opportunity', category: 'InMails', platform: 'linkedin', type: 'inmail', description: 'Job opportunity pitch', path: 'linkedin/inmails/job_opportunity.md' },

  // LinkedIn Comments
  { id: 'li-cm-engage', name: 'Thoughtful Engagement', category: 'Comments', platform: 'linkedin', type: 'comment', description: 'Engaging comment', path: 'linkedin/comments/thoughtful_engagement.md' },
  { id: 'li-cm-question', name: 'Question Comment', category: 'Comments', platform: 'linkedin', type: 'comment', description: 'Ask a question', path: 'linkedin/comments/question_comment.md' },
  { id: 'li-cm-congrats', name: 'Congratulations', category: 'Comments', platform: 'linkedin', type: 'comment', description: 'Congratulate someone', path: 'linkedin/comments/congratulations.md' },

  // Twitter Templates
  // DMs
  { id: 'tw-dm-cold', name: 'Cold DM', category: 'DMs', platform: 'twitter', type: 'dm', description: 'Cold Twitter DM', path: 'twitter/dms/cold_dm.md' },
  { id: 'tw-dm-follow', name: 'After Follow', category: 'DMs', platform: 'twitter', type: 'dm', description: 'DM after following', path: 'twitter/dms/after_follow.md' },
  { id: 'tw-dm-mutual', name: 'Mutual Follower', category: 'DMs', platform: 'twitter', type: 'dm', description: 'Mutual followers DM', path: 'twitter/dms/mutual_follower.md' },
  { id: 'tw-dm-reply', name: 'Reply to Tweet', category: 'DMs', platform: 'twitter', type: 'dm', description: 'DM after tweet reply', path: 'twitter/dms/reply_to_tweet.md' },
  { id: 'tw-dm-collab', name: 'Collaboration', category: 'DMs', platform: 'twitter', type: 'dm', description: 'Propose collaboration', path: 'twitter/dms/collaboration.md' },
  { id: 'tw-dm-thanks', name: 'Thank You', category: 'DMs', platform: 'twitter', type: 'dm', description: 'Thank you DM', path: 'twitter/dms/thank_you.md' },
  { id: 'tw-dm-founder', name: 'Founder Outreach', category: 'DMs', platform: 'twitter', type: 'dm', description: 'Reach founders', path: 'twitter/dms/founder_outreach.md' },
  { id: 'tw-dm-thought', name: 'Thought Leader', category: 'DMs', platform: 'twitter', type: 'dm', description: 'Reach thought leaders', path: 'twitter/dms/thought_leader_outreach.md' },
  { id: 'tw-dm-influencer', name: 'Influencer Outreach', category: 'DMs', platform: 'twitter', type: 'dm', description: 'Reach influencers', path: 'twitter/dms/influencer_outreach.md' },
  { id: 'tw-dm-expert', name: 'Expert Consultation', category: 'DMs', platform: 'twitter', type: 'dm', description: 'Request expertise', path: 'twitter/dms/expert_consultation.md' },
  { id: 'tw-dm-podcast', name: 'Podcast Guest', category: 'DMs', platform: 'twitter', type: 'dm', description: 'Invite to podcast', path: 'twitter/dms/podcast_guest.md' },
  { id: 'tw-dm-investor', name: 'Investor Intro', category: 'DMs', platform: 'twitter', type: 'dm', description: 'Investor introduction', path: 'twitter/dms/investor_intro.md' },

  // Twitter Tweets/Replies
  { id: 'tw-tw-engage', name: 'Engagement Reply', category: 'Tweets', platform: 'twitter', type: 'tweet', description: 'Engaging reply', path: 'twitter/tweets/engagement_reply.md' },
  { id: 'tw-tw-quote', name: 'Quote Tweet', category: 'Tweets', platform: 'twitter', type: 'tweet', description: 'Quote tweet template', path: 'twitter/tweets/quote_tweet.md' },
  { id: 'tw-tw-mention', name: 'Mention', category: 'Tweets', platform: 'twitter', type: 'tweet', description: 'Mention someone', path: 'twitter/tweets/mention.md' },
  { id: 'tw-tw-thread', name: 'Thread Starter', category: 'Tweets', platform: 'twitter', type: 'tweet', description: 'Start a thread', path: 'twitter/tweets/thread_starter.md' },
  { id: 'tw-re-value', name: 'Value Add Reply', category: 'Replies', platform: 'twitter', type: 'reply', description: 'Add value in reply', path: 'twitter/replies/value_add.md' },
  { id: 'tw-re-question', name: 'Question Reply', category: 'Replies', platform: 'twitter', type: 'reply', description: 'Ask in reply', path: 'twitter/replies/question.md' },
  { id: 'tw-re-agree', name: 'Agreement Reply', category: 'Replies', platform: 'twitter', type: 'reply', description: 'Agree and expand', path: 'twitter/replies/agreement.md' },
  { id: 'tw-re-insight', name: 'Insight Reply', category: 'Replies', platform: 'twitter', type: 'reply', description: 'Share insight', path: 'twitter/replies/insight.md' },
  { id: 'tw-re-build', name: 'Build in Public', category: 'Replies', platform: 'twitter', type: 'reply', description: 'Build in public reply', path: 'twitter/replies/build_in_public.md' },
  { id: 'tw-re-milestone', name: 'Milestone Congrats', category: 'Replies', platform: 'twitter', type: 'reply', description: 'Congratulate milestone', path: 'twitter/replies/milestone_congrats.md' },

  // Instagram Templates
  // DMs
  { id: 'ig-dm-cold', name: 'Cold DM', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Cold Instagram DM', path: 'instagram/dms/cold_dm.md' },
  { id: 'ig-dm-follow', name: 'After Follow', category: 'DMs', platform: 'instagram', type: 'dm', description: 'DM after following', path: 'instagram/dms/after_follow.md' },
  { id: 'ig-dm-story', name: 'Story Reply', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Reply to story', path: 'instagram/dms/story_reply.md' },
  { id: 'ig-dm-mutual', name: 'Mutual Follower', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Mutual followers DM', path: 'instagram/dms/mutual_follower.md' },
  { id: 'ig-dm-collab', name: 'Collaboration', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Propose collaboration', path: 'instagram/dms/collaboration.md' },
  { id: 'ig-dm-biz', name: 'Business Inquiry', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Business inquiry', path: 'instagram/dms/business_inquiry.md' },
  { id: 'ig-dm-thanks', name: 'Thank You', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Thank you DM', path: 'instagram/dms/thank_you.md' },
  { id: 'ig-dm-influencer', name: 'Influencer Outreach', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Reach influencers', path: 'instagram/dms/influencer_outreach.md' },
  { id: 'ig-dm-brand', name: 'Brand Collaboration', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Brand partnership', path: 'instagram/dms/brand_collaboration.md' },
  { id: 'ig-dm-creator', name: 'Creator Partnership', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Creator collab', path: 'instagram/dms/creator_partnership.md' },
  { id: 'ig-dm-expert', name: 'Expert Connect', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Connect with expert', path: 'instagram/dms/expert_connect.md' },
  { id: 'ig-dm-product', name: 'Product Feature', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Product feature request', path: 'instagram/dms/product_feature.md' },
  { id: 'ig-dm-founder', name: 'Founder Connect', category: 'DMs', platform: 'instagram', type: 'dm', description: 'Connect with founder', path: 'instagram/dms/founder_connect.md' },

  // Instagram Comments
  { id: 'ig-cm-engage', name: 'Engagement', category: 'Comments', platform: 'instagram', type: 'comment', description: 'Engaging comment', path: 'instagram/comments/engagement.md' },
  { id: 'ig-cm-compliment', name: 'Compliment', category: 'Comments', platform: 'instagram', type: 'comment', description: 'Compliment post', path: 'instagram/comments/compliment.md' },
  { id: 'ig-cm-question', name: 'Question', category: 'Comments', platform: 'instagram', type: 'comment', description: 'Ask a question', path: 'instagram/comments/question.md' },
  { id: 'ig-cm-support', name: 'Support', category: 'Comments', platform: 'instagram', type: 'comment', description: 'Show support', path: 'instagram/comments/support.md' },
  { id: 'ig-cm-value', name: 'Value Add', category: 'Comments', platform: 'instagram', type: 'comment', description: 'Add value', path: 'instagram/comments/value_add.md' },
  { id: 'ig-cm-appreciate', name: 'Appreciation', category: 'Comments', platform: 'instagram', type: 'comment', description: 'Show appreciation', path: 'instagram/comments/appreciation.md' },

  // Instagram Stories
  { id: 'ig-st-reply', name: 'Story Reply', category: 'Stories', platform: 'instagram', type: 'story', description: 'Reply to story', path: 'instagram/stories/story_reply.md' },
  { id: 'ig-st-mention', name: 'Story Mention', category: 'Stories', platform: 'instagram', type: 'story', description: 'Mention in story', path: 'instagram/stories/story_mention.md' },
  { id: 'ig-st-react', name: 'Story Reaction', category: 'Stories', platform: 'instagram', type: 'story', description: 'React to story', path: 'instagram/stories/story_reaction.md' },

  // Email Templates
  // Outreach
  { id: 'em-out-cold', name: 'Cold Email', category: 'Outreach', platform: 'email', type: 'outreach', description: 'Cold email outreach', path: 'email/outreach/cold_email.md' },
  { id: 'em-out-warm', name: 'Warm Intro', category: 'Outreach', platform: 'email', type: 'outreach', description: 'Warm introduction', path: 'email/outreach/warm_intro.md' },
  { id: 'em-out-referral', name: 'Referral Intro', category: 'Outreach', platform: 'email', type: 'outreach', description: 'Referral introduction', path: 'email/outreach/referral_intro.md' },
  { id: 'em-out-partner', name: 'Partnership', category: 'Outreach', platform: 'email', type: 'outreach', description: 'Partnership proposal', path: 'email/outreach/partnership.md' },
  { id: 'em-out-investor', name: 'Investor Pitch', category: 'Outreach', platform: 'email', type: 'outreach', description: 'Investor pitch email', path: 'email/outreach/investor_pitch.md' },

  // Email Follow-ups
  { id: 'em-fu-1', name: 'No Response 1', category: 'Follow-up', platform: 'email', type: 'followup', description: 'First follow-up', path: 'email/follow-up/no_response_1.md' },
  { id: 'em-fu-2', name: 'No Response 2', category: 'Follow-up', platform: 'email', type: 'followup', description: 'Second follow-up', path: 'email/follow-up/no_response_2.md' },
  { id: 'em-fu-final', name: 'Final Follow-up', category: 'Follow-up', platform: 'email', type: 'followup', description: 'Last follow-up', path: 'email/follow-up/no_response_final.md' },
  { id: 'em-fu-meeting', name: 'After Meeting', category: 'Follow-up', platform: 'email', type: 'followup', description: 'Post-meeting follow-up', path: 'email/follow-up/after_meeting.md' },
  { id: 'em-fu-call', name: 'After Call', category: 'Follow-up', platform: 'email', type: 'followup', description: 'Post-call follow-up', path: 'email/follow-up/after_call.md' },
  { id: 'em-fu-check', name: 'Check In', category: 'Follow-up', platform: 'email', type: 'followup', description: 'Check in email', path: 'email/follow-up/check_in.md' },

  // Email Promotional
  { id: 'em-pr-launch', name: 'Product Launch', category: 'Promotional', platform: 'email', type: 'promotional', description: 'Product launch email', path: 'email/promotional/product_launch.md' },
  { id: 'em-pr-feature', name: 'Feature Announcement', category: 'Promotional', platform: 'email', type: 'promotional', description: 'New feature email', path: 'email/promotional/feature_announcement.md' },
  { id: 'em-pr-discount', name: 'Discount Offer', category: 'Promotional', platform: 'email', type: 'promotional', description: 'Discount offer email', path: 'email/promotional/discount_offer.md' },
  { id: 'em-pr-webinar', name: 'Webinar Invite', category: 'Promotional', platform: 'email', type: 'promotional', description: 'Webinar invitation', path: 'email/promotional/webinar_invite.md' },

  // Email Newsletters
  { id: 'em-nl-weekly', name: 'Weekly Digest', category: 'Newsletters', platform: 'email', type: 'newsletter', description: 'Weekly newsletter', path: 'email/newsletters/weekly_digest.md' },
  { id: 'em-nl-monthly', name: 'Monthly Update', category: 'Newsletters', platform: 'email', type: 'newsletter', description: 'Monthly update', path: 'email/newsletters/monthly_update.md' },
  { id: 'em-nl-announce', name: 'Announcement', category: 'Newsletters', platform: 'email', type: 'newsletter', description: 'Announcement email', path: 'email/newsletters/announcement.md' },
]

// Get templates by platform
export function getTemplatesByPlatform(platform: Template['platform']): Template[] {
  return templates.filter(t => t.platform === platform)
}

// Get templates grouped by category
export function getTemplatesGroupedByCategory(platform: Template['platform']): Record<string, Template[]> {
  const platformTemplates = getTemplatesByPlatform(platform)
  return platformTemplates.reduce((acc, t) => {
    if (!acc[t.category]) acc[t.category] = []
    acc[t.category].push(t)
    return acc
  }, {} as Record<string, Template[]>)
}

// Platform stats
export const templateStats = {
  linkedin: templates.filter(t => t.platform === 'linkedin').length,
  twitter: templates.filter(t => t.platform === 'twitter').length,
  instagram: templates.filter(t => t.platform === 'instagram').length,
  email: templates.filter(t => t.platform === 'email').length,
  total: templates.length,
}
