---
layout: page
title: Contact Us
---

<div class="max-w-4xl mx-auto">
  <!-- Hero Section -->
  <div class="text-center mb-12">
    <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">Let's Work Together</h1>
    <p class="text-xl text-gray-600">
      Ready to transform your business? Get in touch with our team to discuss your project.
    </p>
  </div>

  <div class="grid md:grid-cols-2 gap-8 mb-12">
    <!-- Contact Form -->
    <div class="bg-white rounded-lg shadow-lg p-8">
      <h2 class="text-2xl font-semibold text-gray-900 mb-6">Send Us a Message</h2>
      <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" class="space-y-4">
        <div>
          <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Name *</label>
          <input
            type="text"
            id="name"
            name="name"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            placeholder="Your name"
          />
        </div>

        <div>
          <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email *</label>
          <input
            type="email"
            id="email"
            name="email"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            placeholder="your@email.com"
          />
        </div>

        <div>
          <label for="company" class="block text-sm font-medium text-gray-700 mb-1">Company</label>
          <input
            type="text"
            id="company"
            name="company"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            placeholder="Your company name"
          />
        </div>

        <div>
          <label for="subject" class="block text-sm font-medium text-gray-700 mb-1">Subject *</label>
          <input
            type="text"
            id="subject"
            name="subject"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            placeholder="How can we help?"
          />
        </div>

        <div>
          <label for="message" class="block text-sm font-medium text-gray-700 mb-1">Message *</label>
          <textarea
            id="message"
            name="message"
            rows="5"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            placeholder="Tell us about your project..."
          ></textarea>
        </div>

        <button
          type="submit"
          class="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-6 py-3 rounded-lg font-semibold transition-all duration-200 shadow-lg hover:shadow-xl"
        >
          Send Message
        </button>
      </form>
      <p class="text-sm text-gray-500 mt-4">
        * Required fields. We'll respond within 24 hours.
      </p>
    </div>

    <!-- Contact Information -->
    <div class="space-y-6">
      <!-- Contact Details -->
      <div class="bg-gradient-to-br from-blue-600 to-purple-600 rounded-lg shadow-lg p-8 text-white">
        <h2 class="text-2xl font-semibold mb-6">Contact Information</h2>

        <div class="space-y-4">
          <div class="flex items-start">
            <svg class="w-6 h-6 mr-3 mt-1 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            <div>
              <h3 class="font-medium mb-1">Email</h3>
              <a href="mailto:hello@yourcompany.com" class="text-blue-100 hover:text-white">
                hello@yourcompany.com
              </a>
            </div>
          </div>

          <div class="flex items-start">
            <svg class="w-6 h-6 mr-3 mt-1 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
            </svg>
            <div>
              <h3 class="font-medium mb-1">Phone</h3>
              <a href="tel:+15555551234" class="text-blue-100 hover:text-white">
                +1 (555) 555-1234
              </a>
            </div>
          </div>

          <div class="flex items-start">
            <svg class="w-6 h-6 mr-3 mt-1 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            <div>
              <h3 class="font-medium mb-1">Location</h3>
              <p class="text-blue-100">
                123 Main Street<br/>
                Suite 100<br/>
                Boston, MA 02101
              </p>
            </div>
          </div>

          <div class="flex items-start">
            <svg class="w-6 h-6 mr-3 mt-1 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <div>
              <h3 class="font-medium mb-1">Business Hours</h3>
              <p class="text-blue-100">
                Monday - Friday: 9:00 AM - 6:00 PM<br/>
                Saturday - Sunday: Closed
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Social Links -->
      <div class="bg-white rounded-lg shadow-lg p-8">
        <h3 class="text-xl font-semibold text-gray-900 mb-4">Follow Us</h3>
        <div class="flex space-x-4">
          <a href="https://twitter.com/yourcompany" target="_blank" rel="noopener noreferrer"
             class="text-gray-600 hover:text-blue-600 transition-colors">
            <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24">
              <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/>
            </svg>
          </a>
          <a href="https://linkedin.com/company/yourcompany" target="_blank" rel="noopener noreferrer"
             class="text-gray-600 hover:text-blue-700 transition-colors">
            <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24">
              <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.761 0 5-2.239 5-5v-14c0-2.761-2.239-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
            </svg>
          </a>
          <a href="https://github.com/yourcompany" target="_blank" rel="noopener noreferrer"
             class="text-gray-600 hover:text-gray-900 transition-colors">
            <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
          </a>
        </div>
      </div>

      <!-- Quick Links -->
      <div class="bg-gray-50 rounded-lg p-6">
        <h3 class="text-xl font-semibold text-gray-900 mb-4">Quick Links</h3>
        <ul class="space-y-2">
          <li>
            <a href="/docs/getting-started/" class="text-blue-600 hover:text-blue-800">
              Getting Started Guide →
            </a>
          </li>
          <li>
            <a href="/case-studies/" class="text-blue-600 hover:text-blue-800">
              View Case Studies →
            </a>
          </li>
          <li>
            <a href="/blog/" class="text-blue-600 hover:text-blue-800">
              Read Our Blog →
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <!-- FAQ Section -->
  <div class="bg-white rounded-lg shadow-lg p-8">
    <h2 class="text-2xl font-semibold text-gray-900 mb-6">Frequently Asked Questions</h2>
    <div class="space-y-4">
      <div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">What is your typical project timeline?</h3>
        <p class="text-gray-600">
          Project timelines vary based on scope and complexity. Most projects range from 4-12 weeks.
          We'll provide a detailed timeline during our initial consultation.
        </p>
      </div>
      <div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">Do you offer ongoing support?</h3>
        <p class="text-gray-600">
          Yes, we offer various support and maintenance packages to ensure your solution continues
          to perform optimally after launch.
        </p>
      </div>
      <div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">What industries do you work with?</h3>
        <p class="text-gray-600">
          We work with clients across various industries including technology, healthcare, finance,
          e-commerce, and more.
        </p>
      </div>
    </div>
  </div>
</div>
