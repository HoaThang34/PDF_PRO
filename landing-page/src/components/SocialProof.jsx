const partners = [
  'FPT', 'VNG', 'Vingroup', 'Vietcombank', 'Viettel', 'MBBank'
]

const reviews = [
  { name: 'Nguyễn Văn A', role: 'Developer', text: 'Công cụ xử lý PDF tốt nhất tôi từng dùng. Tốc độ xử lý siêu nhanh!' },
  { name: 'Trần Thị B', role: 'Designer', text: 'Tính năng edit PDF rất tuyệt vời. Tôi có thể chỉnh sửa trực tiếp mà không cần chuyển đổi.' },
  { name: 'Lê Văn C', role: 'Sinh viên', text: 'Miễn phí mà chất lượng không thua kém các phần mềm trả phí. Rất khuyên dùng!' },
]

export default function SocialProof() {
  return (
    <section className="social-proof">
      <div className="container">
        <div className="proof-stats">
          <div className="proof-stat">
            <span className="proof-num">50,000+</span>
            <span className="proof-label">Người dùng đăng ký</span>
          </div>
          <div className="proof-stat">
            <span className="proof-num">1,200,000+</span>
            <span className="proof-label">File đã xử lý</span>
          </div>
          <div className="proof-stat">
            <span className="proof-num">4.9/5</span>
            <span className="proof-label">Đánh giá từ người dùng</span>
          </div>
        </div>

        <div className="proof-partners">
          <span className="proof-partners-label">Được tin dùng bởi</span>
          <div className="partner-logos">
            {partners.map((p) => (
              <div key={p} className="partner-logo">{p}</div>
            ))}
          </div>
        </div>

        <div className="proof-reviews">
          {reviews.map((r, i) => (
            <div key={i} className="review-card">
              <div className="review-stars">★★★★★</div>
              <p className="review-text">"{r.text}"</p>
              <div className="review-author">
                <div className="review-avatar">{r.name[0]}</div>
                <div>
                  <div className="review-name">{r.name}</div>
                  <div className="review-role">{r.role}</div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
