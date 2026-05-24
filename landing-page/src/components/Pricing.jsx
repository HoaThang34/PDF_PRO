const plans = [
  {
    name: 'Miễn phí', price: '0', desc: 'Dành cho cá nhân',
    features: [
      'Xử lý tối đa 10 file/ngày', 'Dung lượng file tối đa 50MB',
      'Merge & Split PDF', 'Nén PDF cơ bản', 'Chuyển đổi PDF',
    ],
    cta: 'Bắt đầu miễn phí', popular: false,
  },
  {
    name: 'Pro', price: '99', desc: 'Dành cho chuyên nghiệp',
    features: [
      'Xử lý không giới hạn', 'Dung lượng file tối đa 2GB',
      'OCR & AI', 'Batch processing', 'API Integration',
      'Watermark & Sign', 'Hỗ trợ ưu tiên',
    ],
    cta: 'Dùng thử 14 ngày', popular: true,
  },
  {
    name: 'Business', price: '299', desc: 'Dành cho doanh nghiệp',
    features: [
      'Tất cả tính năng Pro', 'Team workspace', 'Admin dashboard',
      'Sao lưu & đồng bộ đám mây', 'Priority support 24/7',
      'Custom branding', 'SLA đảm bảo 99.99%',
    ],
    cta: 'Liên hệ bán hàng', popular: false,
  },
]

export default function Pricing() {
  return (
    <section className="pricing" id="pricing">
      <div className="container">
        <div className="section-header">
          <h2>Bảng giá linh hoạt</h2>
          <p>Chọn gói phù hợp nhất với nhu cầu của bạn</p>
          <div className="pricing-toggle">
            <span className="active">Thanh toán tháng</span>
            <span>Thanh toán năm <small>(tiết kiệm 20%)</small></span>
          </div>
        </div>
        <div className="pricing-grid">
          {plans.map((p) => (
            <div key={p.name} className={`pricing-card ${p.popular ? 'pricing-card--popular' : ''}`}>
              {p.popular && <div className="popular-badge">Phổ biến nhất</div>}
              <h3 className="pricing-name">{p.name}</h3>
              <p className="pricing-desc">{p.desc}</p>
              <div className="pricing-price">
                <span className="price-currency">đ</span>
                <span className="price-value">{p.price}</span>
                <span className="price-period">/tháng</span>
              </div>
              <ul className="pricing-features">
                {p.features.map((f) => (
                  <li key={f} className="pricing-feature">✓ {f}</li>
                ))}
              </ul>
              <a href="#!" className={`btn ${p.popular ? 'btn-primary' : 'btn-outline'} btn-full`}>
                {p.cta}
              </a>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
